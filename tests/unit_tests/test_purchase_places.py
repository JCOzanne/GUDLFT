import pytest

from server import competitions


def test_purchase_places_with_enough_points(client):
    client.post('/purchasePlaces', data="john@simplylift.co")
    result = client.post("/purchasePlaces", data={
        "competition": "Spring Festival",
        "club": "Simply Lift",
        "places": "5"
    })
    assert result.status_code == 200
    assert 'Great-booking complete! You booked 5 places.' in result.data.decode()

def test_purchase_more_than_12_places(client):
    result = client.post("/purchasePlaces", data={
        "competition": "Spring Festival",
        "club": "Simply Lift",
        "places": "13"
    })
    assert result.status_code == 200
    assert 'You cannot book more than 12 places!' in result.data.decode()

def test_purchase_places_with_not_enough_points(client):
    client.post("/purchasePlaces", data={"email": "john@simplylift.co"})
    result = client.post("/purchasePlaces", data={
        "competition": "Spring Festival",
        "club": "Simply Lift",
        "places": "14"
    })
    assert result.status_code == 200
    assert 'You do not have enough points!' in result.data.decode()

def test_purchase_less_than_0_places(client):
    client.post("/purchasePlaces", data={"email": "john@simplylift.co"})
    result = client.post("/purchasePlaces", data={
        "competition": "Spring Festival",
        "club": "Simply Lift",
        "places": "-1"}
    )
    assert result.status_code == 200
    assert 'You cannot book less than 0 places!' in result.data.decode()

def test_purchase_places_if_competition_completed(client):
    competition = [c for c in competitions if c['name'] == "Spring Festival"][0]
    competition["numberOfPlaces"] = "0"
    client.post("/purchasePlaces", data={"email": "john@simplylift.co"})
    result = client.post("/purchasePlaces", data={
        "competition": "Spring Festival",
        "club": "Simply Lift",
        "places": "1"
    })
    assert result.status_code == 200
    assert 'The competition is over!' in result.data.decode()

def purchase_places_more_than_available_places(client):
    competition = [c for c in competitions if c['name'] == "Spring Festival"][0]
    competition["numberOfPlaces"] = "25"
    result = client.post("/purchasePlaces", data={
        "competition": "Spring Festival",
        "club": "Simply Lift",
        "places": "30"
    })
    assert result.status_code == 200
    assert 'You cannot book more than the available places!' in result.data.decode()