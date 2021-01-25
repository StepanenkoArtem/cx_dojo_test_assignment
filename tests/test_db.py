# coding=utf-8
"""Testing database interation."""


import pytest
from mysql.connector import connect
from yelpme import settings

TEST_DATASET_YELP = 'tests/dataset/yelp.json'
TEST_DATASET_GOOGLE = 'tests/dataset/googlerated.json'


@pytest.fixture
def database():
    conn = connect(
        host=settings.DB_HOST,
        user=settings.DB_USER,
        passwd=settings.DB_PASSWORD,
    )
    with conn.cursor() as cursor:
        cursor.execute('CREATE DATABASE yelp;')
    yield
    conn.cursor().execute('DROP DATABASE yelp;')


def test_db():
    connection = connect(
        host=settings.DB_HOST,
        user=settings.DB_USER,
        passwd=settings.DB_PASSWORD,
    )
    cursor = connection.cursor()
    cursor.execute("SHOW DATABASES LIKE 'yelp';")
    print(cursor.stored_results)
