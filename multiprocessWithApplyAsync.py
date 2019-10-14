from multiprocessing import Pool, get_logger, log_to_stderr
from os import getpid
from time import sleep
from random import random
import logging

MAX_WORKERS = 5


class TestingMpApplyAsync(object):
    def __init__(self):
        """
        Initiates a pool of processes.
        """
        self.pool = Pool(processes=MAX_WORKERS, )

    def generate_some_work(self):
        """
        This method writes some messages to the queue.
        """
        for i in range(50):
            self.pool.apply_async(self.worker_main, ["First item for loop %d" % i])
            self.pool.apply_async(self.worker_main, ["2nd item for loop %d" % i])

    def worker_main(self, msg):
        """
        This function will be executed by a subprocess of the pool.
        It can't be integrated to a class because you can't pass a method of
        an object instance to apply_async(), you need to use a function.
        """
        print("{0} retrieved: {1}".format(getpid(), msg))
        # simulate some random length operations
        sleep(random())

    def set_logging(self):
        log_to_stderr()
        logger = get_logger()
        logger.setLevel(logging.INFO)


# Warning from Python documentation:
# Functionality within this package requires that the __main__ module be
# importable by the children. This means that some examples, such as the
# multiprocessing.Pool examples will not work in the interactive interpreter.
if __name__ == '__main__':
    mp_class = TestingMpApplyAsync()
    mp_class.generate_some_work()
    # Waits a bit for the child processes to do some work
    # because when the parent exits, childs are terminated.
    sleep(10)
