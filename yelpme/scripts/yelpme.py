#!/usr/bin/env python
# coding=utf-8

"""Main module."""
import sys

import click
from yelpme import engine, logging, settings


@click.command()
@click.argument(
    'phrase',
)
@click.argument(
    'region',
)
@click.option(
    '--rows',
    help='Quantity rows you want to retrive. 50 rows by default',
    default=settings.DEFAULT_ROWS_NUM,
)
def main(phrase, region, rows):
    """Get parameters from commandline.

    PHRASE - A phrase you want to search about on yelp.com.
    REGION - A region in which you want to get data.
    ROWS - Quantity of rows you want to retrive
    """
    try:
        engine.run(
            phrase=phrase,
            region=region,
            rows_num=rows,
        )
    except (logging.YelpmeException) as error:
        logging.error(error)
        logging.debug(error.__cause__)
        sys.exit(error.exit_code)


if __name__ == '__main__':
    main()
