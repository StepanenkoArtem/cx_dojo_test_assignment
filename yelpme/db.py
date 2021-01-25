# coding=utf-8
"""Database interaction module."""

from mysql.connector import Error, connect
from yelpme import logging, settings, sql


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


def create_server_connection(db_host, db_user, db_passwd):
    """Create database server connestion.

    Args:
        db_host : str
            database hostname.
        db_user : str
            database username
        db_passwd : str
            databse password

    Returns:
        connection : object
            established server connection

    Raises:
        DBError : Exception
    """
    connection = None
    try:
        connection = connect(
            host=db_host,
            user=db_user,
            passwd=db_passwd,
        )
    except Error as err:
        raise DBError('Cannot connect to MySQL Server') from err
    return connection


def create_db_connection(db_host, db_user, db_passwd, db_name):
    """Create database connection.

    Args:
        db_host: str
            database hostname.
        db_user: str
            database username
        db_passwd: str
            databse password
        db_name : str
            database name

    Returns:
        connection : object
            established connection

    Raises:
        DBError : Exception
    """
    try:
        connection = connect(
            host=db_host,
            user=db_user,
            passwd=db_passwd,
            database=db_name,
        )
    except Error as err:
        raise DBError(
            'Cannot connect to database {0}'.format(db_name),
        ) from err
    return connection


def create_database(connection, db_name):
    """Create database.

    Args:
        connection : object
        db_name : str

    Raises:
        DBError : Exception
    """
    cursor = connection.cursor(prepared=True)
    try:
        cursor.execute(
            'CREATE DATABASE IF NOT EXISTS {0}'.format(db_name),
            )
    except Error as err:
        raise DBError('Cannot create database {0}'.format(db_name)) from err


def execute_query(connection, query):
    """Run single database query.

    Args:
        connection : object
        query : str

    Raises:
        DBError: Exception
    """
    cursor = connection.cursor()
    try:  # noqa: WPS229
        cursor.execute(query)
        connection.commit()
    except Error as err:
        raise DBError('Query {0} failed'.format(query)) from err


def execute_many_query(connection, query, tuples):
    """Run multiple database query.

    Args:
        connection : object
        query : str
        tuples : list of SQL parameters

    Raises:
        DBError: Exception
    """
    cursor = connection.cursor()
    try:  # noqa: WPS229
        cursor.executemany(query, tuples)
        connection.commit()
    except Error as err:
        raise DBError('Query {0} failed'.format(query)) from err


def save(businesses):
    """Save retrived business data to database.

    Args:
        businesses : list

    Return:
        None
    """
    connection = create_server_connection(
        db_host=settings.DB_HOST,
        db_user=settings.DB_USER,
        db_passwd=settings.DB_PASSWORD,
    )

    # Create database
    create_database(connection, settings.DB_NAME)

    # Close server connection
    connection.close()

    # Create database connection
    connection = create_db_connection(
        db_host=settings.DB_HOST,
        db_user=settings.DB_USER,
        db_passwd=settings.DB_PASSWORD,
        db_name=settings.DB_NAME,
    )

    # Create tables
    execute_query(connection, sql.create_zip_codes_table_query)
    execute_query(connection, sql.create_cities_table_query)
    execute_query(connection, sql.create_businesses_table_query)
    execute_query(connection, sql.create_tags_table_query)
    execute_query(connection, sql.create_business_on_tags_table_query)

    # Insert zip codes
    zip_codes = {
        (business.get('location')['zip_code'],)
        for business in businesses
    }

    execute_many_query(connection, sql.insert_zip_codes, list(zip_codes))

    # Insert cites
    cities = {
        (business.get('location')['city'],)
        for business in businesses
    }
    execute_many_query(connection, sql.insert_cities, list(cities))

    # Insert tags
    tags = set()
    for business in businesses:
        for category in business.get('categories'):
            tags.add((category['alias'], category['title']))

    execute_many_query(connection, sql.insert_tags, tuple(tags))

    # Insert business

    # Insert tags of business
    tags_of_business = []

    for business in businesses:
        for business_tags in business['categories']:
            tags_of_business.append((business['name'], business_tags['alias']))

    execute_many_query(
        connection,
        sql.insert_business_on_tags,
        tags_of_business,
    )
