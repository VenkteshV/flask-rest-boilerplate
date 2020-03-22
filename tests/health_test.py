"""
To run the tests type,
$ nosetests --verbose
"""

from nose.tools import assert_true
import requests

BASE_URL = "http://localhost:5000"

def test_health():
    response = requests.get('%s/health' % (BASE_URL))
    assert_true(response.ok)