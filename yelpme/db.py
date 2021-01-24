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
    try:
        with connect(
            host=settings.DB_HOST,
            user=settings.DB_USER,
            password=settings.DB_PASSWORD,
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute('SHOW DATABASES;')
    except Error as err:
        raise DBError('Can not connect to MySQL Server') from err
