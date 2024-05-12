import logging
import os
import sys
import globals

from .file_dir_operations import *

API_LOGS = "/logs"


class Logger:
    def __init__(self, logger_name: str):
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.DEBUG)
        self.ROOT_PATH = os.getcwd()

        self.filehandler_factory(logger_name)

    def filehandler_factory(self, logger_name):
        self.logger_filehandler = self.filehandler(logger_name)
        formatter = self.set_formatter()
        self.logger_filehandler.setFormatter(formatter)
        self.logger.addHandler(self.logger_filehandler)

    def __set_logger_DIR(self, filename):
        logs_dir_path = self.ROOT_PATH + API_LOGS

        if not FileOperations.does_file_or_dir_exists(logs_dir_path):
            DIROperations.make_dir(logs_dir_path)

        filename = logs_dir_path + f"/{filename}.log"
        return filename

    def filehandler(self, filename: str) -> logging.FileHandler:
        filename = self.__set_logger_DIR(filename)
        logger_filehandler = logging.FileHandler(
            filename=filename, encoding="utf-8", mode="w")
        logger_filehandler.setLevel(logging.DEBUG)
        return logger_filehandler

    # # Stream Logs code - This is used to print the logs onto STDOUT
    # def stream_filehandler_factory(self):
    #     self.logger_stream_filehandler = self.stream_filehandler()
    #     formatter = self.set_formatter()
    #     self.logger_stream_filehandler.setFormatter(formatter)
    #     self.logger.addHandler(self.logger_stream_filehandler)

    # def stream_filehandler(self) -> logging.StreamHandler:
    #     logger_stream_filehandler = logging.StreamHandler(sys.stdout)
    #     logger_stream_filehandler.setLevel(logging.DEBUG)
    #     return logger_stream_filehandler

    def set_formatter(self):
        formatter = logging.Formatter(
            fmt="[%(asctime)s] - [%(levelname)8s] - [ %(name)s ] - [ %(filename)s ] - [ line-no: %(lineno)d ] --- %(message)s", datefmt='%Y-%m-%d %I:%M:%S %p', )
        return formatter

    def get_logger(self):
        return self.logger


class LogReporterUtils:
    @staticmethod
    def get_current_test():
        return os.environ.get(
            'PYTEST_CURRENT_TEST').split("::")[2].split(" ")[0]

    @staticmethod
    def logger_initialization():
        Logger_Reference = globals.LOGGER_REFERENCE
        logger = Logger_Reference(
            LogReporterUtils.get_current_test()).get_logger()
        return logger
