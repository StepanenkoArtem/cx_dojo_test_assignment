
import pytest
from yelpme import api_requests


@pytest.mark.parametrize(
    'phrase', ['', '  ', '1111'],
)
@pytest.mark.xfail
def test_request_yelp(phrase, location):
    with pytest.raises(api_requests.ApiRequestError):
        api_requests.get_yelp(phrase, 'san francisco')
