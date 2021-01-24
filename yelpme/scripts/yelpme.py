#!/usr/bin/env python
# coding=utf-8

"""Main module."""
import logging
import sys

import click
import yelpme
from yelpme import engine, settings


@click.command()
@click.argument(
    'phrase',
)
@click.argument(
    'location',
)
@click.option(
    '--limit',
    help='Quantity rows you want to retrive. 50 rows by default',
    default=settings.DEFAULT_ROWS_NUM,
)
def main(phrase, location, limit):
    """Get parameters from commandline.

    PHRASE - A phrase you want to search about on yelp.com.
    LOCATION - A region in which you want to get data.
    LIMIT - Quantity of rows you want to retrive
    """
    yelpme.logging.setup()

    try:
        engine.run(
            phrase=phrase,
            location=location,
            limit=limit,
        )
    except (yelpme.logging.YelpmeException) as error:
        logging.error(error)
        logging.debug(error.__cause__)
        sys.exit(error.exit_code)


if __name__ == '__main__':
    main()
