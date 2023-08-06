import logging
import sys


def get_logger(name: str) -> logging.Logger:
    """Initializes a logging.Logger object and formatting.

    :return: logging.Logger
    """
    logger = logging.getLogger(name)
    handler = logging.StreamHandler(sys.stderr)
    formatter = logging.Formatter(fmt="%(name)s:%(levelname)s:%(asctime):%(message)s")
    handler.setFormatter(formatter)

    return logger
