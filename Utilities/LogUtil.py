# --- refer project2 >loggingTest.py for understanding of logger
import logging
import time

class Logger():

    def __init__(self, logger, file_level=logging.INFO):
        # create or retrieve a logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # 1. create handler
        # generate run time file name
        curr_time = time.strftime("%Y-%m-%d")
        self.LogFileName = '..\\Logs\\log' + curr_time + '.txt'

        # "a" to append the logs in the same file, "w" to generate new log and delete old one
        fileHandler = logging.FileHandler(self.LogFileName, mode="a")                   # it will configure the logger

        # 2. specify the format
        formatter = logging.Formatter('%(asctime)s - %(filename)s:[%(lineno)s] - [%(levelname)s] - %(message)s')

        # 3. set defined format (formatter) for the handler
        fileHandler.setFormatter(formatter)
        fileHandler.setLevel(file_level)

        # 4. add handler to the logger
        self.logger.addHandler(fileHandler)