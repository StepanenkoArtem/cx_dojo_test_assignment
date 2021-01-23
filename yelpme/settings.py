# coding=utf-8
"""Yelpme settings."""

# Default numbers of rows per request getting from yelp.com
DEFAULT_ROWS_NUM = 50

# Necessary business data
FIELDS = (
    'name',
    'phone',
    'website',
    'tags',
    'addres',
    'city',
    'zipcode',
    'coordinates',
    'rating',
    'google_rating',
)
