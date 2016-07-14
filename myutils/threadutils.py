# /usr/bin/python
# -*- coding:utf-8 -*-
"""
    Created by qinshuang on 6/12/16.
"""
import multiprocessing
import Queue
import threading
import logging
import time

logger = logging.getLogger(__file__)


class ThreadPool(object):
    '''
    This is a very VERY basic threadpool implementation
    This was made instead of using multiprocessing ThreadPool because
    we want to set max queue size and we want to daemonize threads (neither
    is exposed in the stdlib version).

    Since there isn't much use for this class as of right now this implementation
    Only supports daemonized threads and will *not* return results

    TODO: if this is found to be more generally useful it would be nice to pull
    in the majority of code from upstream or from http://bit.ly/1wTeJtM
    '''

    def __init__(self,
                 num_threads=None,
                 queue_size=0, daemon=False):
        # if no count passed, default to number of CPUs
        if num_threads is None:
            num_threads = multiprocessing.cpu_count()
        self.num_threads = num_threads

        # create a task queue of queue_size
        self._job_queue = Queue.Queue(queue_size)

        self._workers = []

        # create worker threads
        for _ in range(num_threads):
            thread = threading.Thread(target=self._thread_target)
            thread.daemon = daemon
            thread.start()
            self._workers.append(thread)

    # intentionally not called "apply_async"  since we aren't keeping track of
    # the return at all, if we want to make this API compatible with multiprocessing
    # threadpool we can in the future, and we won't have to worry about name collision
    def fire_async(self, func, args=None, kwargs=None):
        if args is None:
            args = []
        if kwargs is None:
            kwargs = {}
        try:
            self._job_queue.put_nowait((func, args, kwargs))
            return True
        except Queue.Full:
            return False

    def _thread_target(self):
        while True:
            # 1s timeout so that if the parent dies this thread will die within 1s
            try:
                try:
                    func, args, kwargs = self._job_queue.get(timeout=1)
                    self._job_queue.task_done()  # Mark the task as done once we get it
                except Queue.Empty:
                    continue
            except AttributeError:
                # During shutdown, `queue` may not have an `Empty` atttribute. Thusly,
                # we have to catch a possible exception from our exception handler in
                # order to avoid an unclean shutdown. Le sigh.
                continue
            try:
                logger.debug('ThreadPool executing func: {0} with args:{1}'
                             ' kwargs{2}'.format(func, args, kwargs))
                func(*args, **kwargs)
            except Exception as err:
                logger.debug(err, exc_info=True)

    def add_task(self, func, args=None, kwargs=None, timeout=0):
        """
            向队列中添加任务
        """
        now_time = time.time()
        while True:
            if self.fire_async(func, args, kwargs):
                return True
            if timeout != 0 and time.time() - now_time > timeout:
                logger.info(" Queue 已满，添加任务超时，请检查队列中任务是否完成。")
                return False
