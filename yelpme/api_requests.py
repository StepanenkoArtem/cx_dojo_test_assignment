"""API Requests module."""

import urllib

import requests
import yelpme
from yelpme import settings


class ApiRequestError(yelpme.logging.YelpmeException):
    """ApiRequest Exception."""

    exit_code = 2

    def __init__(self, message):
        """Init ApiRequest Exception.

        Args:
            message : str
                message error
        """
        self.message = message


def clear_data(business):
    cleared = {}
    for field, field_value in business.items():
        if field in settings.FIELDS:
            cleared[field] = field_value
    return cleared


def get_yelp(phrase, location, limit):
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
    try:  # noqa: WPS229
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
    return list(map(clear_data, businesses))


def get_gmp_id(name, *coordinates):
    """Get place_id from googlemaps.

    Args:
        name : str
            business name
        coordinates : tuple
            latitude and longitude of business

    Returns:
        : list
            list of businesess

    Raises:
        ApiRequestError : Exception
            while request error happend
    """
    locationbias = 'point:{0}{1}'.format(*coordinates)

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
    }
    try:  # noqa: WPS229
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
    place = responce.json()['candidates'][0]
    return place['place_id']


def get_gmp_details(place_id):
    request_gmp_detail_params = {
        'fields': 'website,rating',
        'key': settings.GMP_API_KEY,
        'place_id': place_id,
    }
    request_gmp_detail_headers = {
        'Host': 'maps.googleapis.com',
        'Connection': 'keep-alive',
    }
    responce = requests.get(
        settings.GMP_DETAILS_API_URL,
        params=urllib.parse.urlencode(request_gmp_detail_params),
        headers=request_gmp_detail_headers,
    )
    details = responce.json()['result']
    details['google_rating'] = details.pop('rating')

    return details
