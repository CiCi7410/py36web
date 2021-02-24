import logging
from config.path import logs_path
import os


def my_logger(name="py36",
              logger_level="INFO",
              fmt_str="%(asctime)s-%(levelname)s:%(name)s:%(message)s:%(filename)s,%(lineno)s",
              handle_level="INFO",
              file=True,
              file_handle_level="INFO",
              file_name="file_handle"):
    logger = logging.getLogger(name)
    logger.setLevel(logger_level)
    fmt = logging.Formatter(fmt_str)
    handle = logging.StreamHandler()
    handle.setLevel(handle_level)
    handle.setFormatter(fmt)
    logger.addHandler(handle)
    if file:
        file_handle = logging.FileHandler(file_name)
        file_handle.setLevel(file_handle_level)
        file_handle.setFormatter(fmt)
        logger.addHandler(file_handle)
    return logger

