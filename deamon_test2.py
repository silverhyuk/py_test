import time
import logging

import os
import signal

import argparse

from concurrent.futures import ProcessPoolExecutor

class S3Checker:
    SONG_LIST = ["S3Checker1", "S3Checker2", "S3Checker3"]

    def __init__(self, log_file=None):
        logging.basicConfig(level=logging.INFO, format='%(message)s')
        self.logger = logging.getLogger("S3Checker")
        self.log_file = log_file

        if log_file:
            self.log_handler = logging.FileHandler(self.log_file)
            self.logger.addHandler(self.log_handler)

        self.__stop = False

        signal.signal(signal.SIGINT, self.stop)
        signal.signal(signal.SIGTERM, self.stop)

    def main(self):
        i = 0
        self.logger.info("Start Singing, PID {0}".format(os.getpid()))
        while not self.__stop:
            self.logger.info(self.SONG_LIST[i % len(self.SONG_LIST)])
            i += 1
            time.sleep(1)

    def stop(self, signum, frame):
        self.__stop = True
        self.logger.info("Receive Signal {0}".format(signum))
        self.logger.info("Stop Singing")

class S3DownLoader:
    executor_processes = ProcessPoolExecutor(4)
    def init(self):

    def run(self):

    def stop(self, signum, frame):
        self.__stop = True
        self.logger.info("Receive Signal {0}".format(signum))
        self.logger.info("Stop Singing")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--log", help="log filename", default=None)
    args = parser.parse_args()

    s3_checker = S3Checker(args.log)
    s3_checker.main()
