import pytest

from server import app, loadClubs, loadCompetitions

@pytest.fixture
def client():
    app.config["TESTING"] = True
    return app.test_client()

@pytest.fixture(autouse=True)
def reset_data():
    from server import clubs, competitions
    clubs[:] = loadClubs()
    competitions[:] = loadCompetitions()