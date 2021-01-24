# coding=utf-8
"""Yelpme settings."""

import os

from dotenv import load_dotenv

load_dotenv()

# YELP API Settings
DEFAULT_ROWS_NUM = 50
YELP_API_URL = 'https://api.yelp.com/v3/businesses/search'
YELP_API_KEY = os.environ.get('YELPME_YELPAPI_KEY')

# Coogle Places API Settings
GMP_API_KEY = os.environ.get('YELPME_GMPAPI_KEY')
GMP_ID_API_URL = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json'
GMP_DETAILS_API_URL = 'https://maps.googleapis.com/maps/api/place/details/json'

# Database settings
DB_HOST = 'localhost'
DB_NAME = 'yelp'
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')

# Necessary businesses data
FIELDS = (
    'name',
    'phone',
    'website',
    'categories',
    'location',
    'city',
    'zip_code',
    'coordinates',
    'rating',
    'google_rating',
)
