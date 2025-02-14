import pytest
from server import app

@pytest.fixture
def client():
    """
    Provides a Flask test client for integration testing.
    :return: A test client instance for the Flask app.
    """
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client