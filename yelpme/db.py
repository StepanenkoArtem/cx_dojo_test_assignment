# coding=utf-8
"""Database interaction module."""

from mysql.connector import Error, connect
from yelpme import logging, settings


class DBError(logging.YelpmeException):
    """Database Error Exception."""

    exit_code = 3

    def __init__(self, message):
        """Init Database Exception.

        Args:
            message : str
                message error
        """
        self.message = message


def save(businesses):
    """Save retrived business data to database.

    Args:
        businesses : list

    Return:
        None

    Raises:
        DBError : Exception
    """
    try:
        with connect(
            host=settings.DB_HOST,
            user=settings.DB_USER,
            password=settings.DB_PASSWORD,
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute('SHOW DATABASES;')
    except Error as err:
        raise DBError('Cannot connect to MySQL Server') from err
