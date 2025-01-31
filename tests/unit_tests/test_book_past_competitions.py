import pytest
import pendulum

from server import competitions

def test_book_past_competitions(client):
    past_competition = [competition for competition in competitions if competition["name"] == "Spring Festival"][0]
    past_competition['date'] = pendulum.yesterday().to_datetime_string()
    result = client.post("/purchasePlaces", data={
        "competition": "Spring Festival",
        "club": "Simply Lift",
        "places": "5"
    })
    assert result.status_code == 200
    assert 'You cannot book places for a past competition !' in result.data.decode()