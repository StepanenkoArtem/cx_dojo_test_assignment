# coding=utf-8

"""Configure logging."""

import logging

LOGFILE = 'yelpme.log'


class YelpmeException(Exception):
    """Logging Error exception."""

    exit_code: int = None

    def __init__(self, message):
        """Init Logging Exception.

        Args:
            message: str
                Exception's message
        """
        super().__init__()
        self.message = message


def setup():
    """Set up logging settings."""
    # Configure console handler
    console_formatter = logging.Formatter(
        fmt='{levelname}:{message}',
        style='{',
    )
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING)
    console_handler.setFormatter(console_formatter)

    #  Configure file handler
    file_handler = logging.FileHandler(LOGFILE)
    file_handler.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter(
        fmt='{asctime}:{levelname}:{message}',
        style='{',
    )
    file_handler.setFormatter(file_formatter)

    logging.basicConfig(
        handlers=(console_handler, file_handler),
        level=logging.DEBUG,
    )
