import pytest

from server import app, loadClubs, loadCompetitions


@pytest.fixture
def client():
    """
    Provides a Flask test client for making requests to the application.
    :return: A test client instance for the Flask app.
    """
    app.config["TESTING"] = True
    return app.test_client()


@pytest.fixture(autouse=True)
def reset_data():
    """
    Resets the clubs and competitions data before each test to ensure test isolation.
    :return: None
    """
    from server import clubs, competitions
    clubs[:] = loadClubs()
    competitions[:] = loadCompetitions()
