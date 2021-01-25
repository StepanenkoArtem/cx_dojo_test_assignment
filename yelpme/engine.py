# coding=utf-8
"""This is an engine module of yelpme."""

from yelpme import api_requests, db


def run(phrase, location, limit):
    """Handle data retrived from source and save it to db.

    Args:
        phrase : str
            phrase for searching business on yelp.com
        location : str
            which region use for search
        limit : int
            number of rows to retrive from yelp.com

    Return: None
    """
    # Get business data from yelp.com
    businesses = api_requests.get_yelp(phrase, location, limit)

    # Get get outstanding data from Google Places
    for business in businesses:
        coordinates = (
            business['coordinates']['latitude'],
            business['coordinates']['longitude'],
        )
        google_place_id = api_requests.get_gmp_id(
            name=business['name'],
            coordinates=coordinates,
        )
        business_gmp_details = api_requests.get_gmp_details(google_place_id)
        business = business.update(business_gmp_details)

    # Save data to DB
    db.save(businesses)
