import signal
import traceback
from datetime import timedelta
from functools import partial, wraps
from multiprocessing import Pool
from os import getpid, kill
from sys import exit
from threading import Condition
from time import sleep
from typing import Callable

from django.core.management.base import BaseCommand

from papyru.utils import limited_runtime, log
from papyru.varspool import add_status, fetch_jobs
from papyru.varspool.types import Job, StatusConflict

from .config import VarspoolJobProcessorConfig
from .types import JobProcessorStatus, JobResult


class JobsManager:
    def __init__(self):
        self._jobs = {}
        self._cv = Condition()

    def count(self):
        return len(self._jobs)

    def add(self, job: Job):
        with self._cv:
            self._jobs[job.id] = job
            self._cv.notify()

    def remove(self, job: Job):
        with self._cv:
            del self._jobs[job.id]
            self._cv.notify()

    def update(self, job, status: str, data: dict = {}) -> Job:
        self._jobs[job.id] = add_status(job, status, data)
        return self._jobs[job.id]

    def wait_for_change(self, timeout: float):
        with self._cv:
            self._cv.wait(timeout=timeout)

    def abort(self, status: str):
        for job in self._jobs.values():
            try:
                log('abort job %d' % job.id)
                add_status(job, status,
                           {'reason': 'graceful command shutdown'})
            except Exception:
                log('[ALERT] could not propagate command shutdown to '
                    'varspool (job id: %d)' % job.id, 'exception')


def loop_until(time_range: timedelta):
    '''
    Decorates a function which performs a single loop step.

    Calls the function as long as the according process has neither
    received SIGTERM nor the given time range has been exceeded.
    '''

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            state = {'received_sigterm': False}

            def handle_sigterm(*args, **kwargs):
                log('caught SIGTERM. will shutdown gracefully.')
                state['received_sigterm'] = True

            signal.signal(signal.SIGTERM, handle_sigterm)

            with limited_runtime(time_range) as has_runtime_left:
                while has_runtime_left() and not state['received_sigterm']:
                    func(*args, **kwargs)
        return wrapper
    return decorator


g_jobs_manager = JobsManager()


def _err_callback(job: Job, ex: Exception):
    log('[ALERT] could not process job %d: %s: %s' % (
        job.id, type(ex).__name__, str(ex)),
        level='error')

    g_jobs_manager.remove(job)


def _succ_callback(job: Job):
    log('finished job %d with status %s.'
        % (job.id, job.status_history.items[-1].status))
    g_jobs_manager.remove(job)


def _get_num_of_jobs_to_fetch(max_parallel_job_count: int):
    return max_parallel_job_count - g_jobs_manager.count()


def handle_job(job: Job,
               job_processor_status: JobProcessorStatus,
               processing_fn: Callable) -> Job:
    '''
    A wrapper for a function processing a job.

    This wrapper function does all the bureaucratic stuff which needs to be
    done around the hard work. It notifies varspool that the job has been
    started and sends the result status after the job has been finished.
    '''

    log('processing job %d.' % job.id)

    try:
        job = g_jobs_manager.update(job, job_processor_status.IN_PROGRESS)
    except StatusConflict:
        log('job %d is already in progress. skipping.' % job.id)
        return job

    try:
        result = processing_fn(job)

    except Exception as ex:
        formatted_traceback = traceback.format_exc()
        formatted_exc = ('uncaught error (%s): %s'
                         % (type(ex).__name__, str(ex)))

        log(formatted_traceback, level='error')
        log(formatted_exc, level='error')

        result = JobResult(
            job_processor_status.FAILED,
            {'reason': formatted_exc, 'traceback': formatted_traceback})

    log('processed job %d. updating varspool.' % job.id)

    return g_jobs_manager.update(job, result.status, result.data)


def wait_for_free_slot(timeout: float):
    g_jobs_manager.wait_for_change(timeout)


def enter_job_loop(config: VarspoolJobProcessorConfig):
    '''
    Main job loop launching a process pool and asynchronously calling
    job processing functions.
    '''

    try:
        log('checking config...')

        if not isinstance(config, VarspoolJobProcessorConfig):
            raise RuntimeError(
                'could not start job loop due to invalid config.')

        log('- queue url: %s' % config.queue_url)

        with Pool(processes=config.max_parallel_job_count) as pool:
            @loop_until(
                time_range=timedelta(minutes=config.max_runtime_in_minutes))
            def wrapper():
                log('fetching jobs...')

                if (g_jobs_manager.count() >= config.max_parallel_job_count):
                    log('too many active jobs. waiting for a free slot.')
                    wait_for_free_slot(config.loop_cooldown_in_seconds)
                    return

                jobs = fetch_jobs(config.queue_url,
                                  config.job_processor_status.OPEN,
                                  _get_num_of_jobs_to_fetch(
                                       config.max_parallel_job_count))

                if len(jobs) == 0:
                    if config.wait_for_further_jobs:
                        log('no jobs to process. waiting...')
                        sleep(config.loop_cooldown_in_seconds)
                    else:
                        kill(getpid(), signal.SIGTERM)
                    return

                for job in jobs:
                    log('dispatching job %d.' % job.id)
                    g_jobs_manager.add(job)

                    pool.apply_async(
                        func=handle_job,
                        args=(job,
                              config.job_processor_status,
                              config.job_handler),
                        callback=_succ_callback,
                        error_callback=partial(_err_callback, job))
                    log('dispatched job %d.' % job.id)
            wrapper()

            # time is over or SIGTERM has been fired to the job processor.
            # abort our work.
            g_jobs_manager.abort(config.job_processor_status.ABORT)

    except Exception as ex:
        log(traceback.format_exc(), level='error')
        log('[ALERT] critical error occurred: %s (%s). '
            'awaiting end of failure backoff...'
            % (type(ex).__name__, str(ex)),
            level='error')

        sleep(config.failure_backoff_in_seconds
              if hasattr(config, 'failure_backoff_in_seconds')
              else (VarspoolJobProcessorConfig
                    .DEFAULT_FAILURE_BACKOFF_IN_SECONDS))
        exit(1)


class VarspoolJobProcessorBaseCommand(BaseCommand):
    config: VarspoolJobProcessorConfig = None

    def handle(self, *args, **kwargs):
        log('varspool job processor started.')

        log('entering job loop.')
        enter_job_loop(self.config)
        log('goodbye.')
