# coding=utf-8
"""This is an engine module of yelpme."""

from yelpme import db, google, settings, yelp


def run(phrase, region, rows_num):
    """Handle data retrived from source and save it to db.

    Args:
        phrase : str
            phrase for searching business on yelp.com
        region : str
            which region use for search
        rows_num : int
            number of rows to retrive from yelp.com

    Return: None
    """
    
    # Get business data from yelp.com
    businesses = yelp.get_businesses(phrase, region, rows_num)
    print(businesses)
    # Get get outstanding data from Google Places
    businesses = map(google.add_details, businesses)
    print(businesses)
    # Save data to DB
    db.save(businesses)
