
from unittest.mock import MagicMock, patch

from yelpme import yelp
from yelpme.engine import run
import json


TEST_DATASET_YELP = 'tests/dataset/yelp.json'
TEST_DATASET_GOOGLE = 'tests/dataset/googlerated.json'


@patch('yelpme.yelp.get_businesses')
@patch('yelpme.google.add_details')
def test_engine_run(mocked_yelp, mocked_google):
    mocked_yelp.return_value = json.load(open(TEST_DATASET_YELP))
    mocked_google.return_value = json.load(open(TEST_DATASET_GOOGLE))
    run('', '', '')
