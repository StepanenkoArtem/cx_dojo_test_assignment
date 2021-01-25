
from yelpme import api_requests


def test_request_yelp():
    limit = 50
    assert api_requests.get_yelp('vegan cafe', 'san francisco', limit)


def test_request_gmp_id():
    coordinates = (37.75235, -122.41925)
    assert api_requests.get_gmp_id('Beloved Cafe', *coordinates)


def test_request_gmp_details():
    place_id = 'ChIJ74VF-qaAhYARb0YeIN1ZqEA'
    assert api_requests.get_gmp_details(place_id)
