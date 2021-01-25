# coding=utf-8
"""API Requests module."""

import urllib

import requests
from yelpme import logging, settings


class ApiRequestError(logging.YelpmeException):
    """ApiRequest Exception."""

    exit_code = 2

    def __init__(self, message):
        """Init ApiRequest Exception.

        Args:
            message : str
                message error
        """
        self.message = message


def _clear_data(business):
    """Filter out necessary data.

    Args:
        business : dict
            raw business data retrived from yelp.com

    Returns:
        cleared : dict
            necessary business data
    """
    cleared = {}
    for field, field_value in business.items():
        if field in settings.FIELDS:
            cleared[field] = field_value
    return cleared


def yelp(phrase, location, limit):
    """Get list of businesses from yelp.com.

    Args:
        phrase : str
            searching phrase
        location : str
            location where search will be
        limit : int
            quantity of requested rows

    Returns:
        : list
            list of businesess

    Raises:
        ApiRequestError : Exception
            while request error happend
    """
    request_yelp_params = {
        'term': phrase,
        'location': location,
        'limit': limit,
        }
    request_yelp_headers = {
        'Authorization': 'Bearer {key}'.format(key=settings.YELP_API_KEY),
        'Connection': 'keep-alive',
        'Host': 'api.yelp.com',
    }
    try:
        responce = requests.get(
            settings.YELP_API_URL,
            headers=request_yelp_headers,
            params=urllib.parse.urlencode(request_yelp_params),
            )
        responce.raise_for_status()
    except (
        requests.RequestException,
        requests.exceptions.HTTPError,
    ) as request_err:
        raise ApiRequestError(
            message="Can't connect to {0}".format(settings.YELP_API_URL),
        ) from request_err
    businesses = responce.json()['businesses']

    # Filter redundant data
    return list(map(_clear_data, businesses))


def google_place_id(name, coordinates):
    """Get place_id from googlemaps.

    Args:
        name : str
            business name
        coordinates : tuple
            latitude and longitude of business

    Returns:
        place_id : str
            GoogleMaps place_id for business

    Raises:
        ApiRequestError : Exception
            while request error happend
    """
    locationbias = 'point:{0},{1}'.format(*coordinates)

    request_gmp_id_params = {
        'fields': 'place_id',
        'inputtype': 'textquery',
        'input': name,
        'locationbias': locationbias,
        'key': settings.GMP_API_KEY,
    }
    request_gmp_id_headers = {
        'Host': 'maps.googleapis.com',
        'Connection': 'keep-alive',
        'Accept-Encoding': 'gzip, deflate, br',
    }
    try:
        responce = requests.get(
            settings.GMP_ID_API_URL,
            params=urllib.parse.urlencode(request_gmp_id_params),
            headers=request_gmp_id_headers,
        )
        responce.raise_for_status()
    except (
        requests.RequestException,
        requests.exceptions.HTTPError,
    ) as request_err:
        raise ApiRequestError(
            message="Can't connect to {0}".format(settings.GMP_ID_API_URL),
        ) from request_err
    try:
        place_id = responce.json()['candidates'][0]['place_id']
    except IndexError as index_err:
        raise ApiRequestError(
            message='GoogleMaps place_Id not found',
        ) from index_err
    return place_id


def google_place_details(place_id):
    """Get place_id from googlemaps.

    Args:
        place_id : str
            GoogleMaps place_id for business

    Returns:
        details : dict
            google_rating and website of business

    Raises:
        ApiRequestError : Exception
            while request error happend
    """
    if not place_id:
        return {}
    request_gmp_detail_params = {
        'fields': 'website,rating',
        'key': settings.GMP_API_KEY,
        'place_id': place_id,
    }
    request_gmp_detail_headers = {
        'Host': 'maps.googleapis.com',
        'Connection': 'keep-alive',
    }
    try:
        responce = requests.get(
            settings.GMP_DETAILS_API_URL,
            params=urllib.parse.urlencode(request_gmp_detail_params),
            headers=request_gmp_detail_headers,
        )
        responce.raise_for_status()
    except (
        requests.RequestException,
        requests.exceptions.HTTPError,
    ) as request_err:
        raise ApiRequestError(
            message="Can't connect to {0}".format(
                settings.GMP_DETAILS_API_URL,
            ),
        ) from request_err
    try:
        details = responce.json()['result']
    except AttributeError as attr_err:
        raise ApiRequestError(
            message='Google Maps details not received',
        ) from attr_err
    details['google_rating'] = details.pop('rating')

    return details
