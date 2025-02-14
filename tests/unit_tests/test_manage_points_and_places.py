import pytest

from server import clubs, competitions


def test_update_club_points_if_purchase_is_ok(client) -> None:
    """
    Tests that club points are correctly deducted after a successful booking.
    :param client: The Flask test client.
    :return: None
    """
    initial_points = int([club for club in clubs if club["name"] == "Simply Lift"][0]["points"])
    result = client.post("/purchasePlaces", data={
        "competition": "Spring Festival",
        "club": "Simply Lift",
        "places": "5"
    })
    assert result.status_code == 200
    assert 'Great-booking complete! You booked 5 places.' in result.data.decode()

    updated_points = int([club for club in clubs if club["name"] == "Simply Lift"][0]["points"])
    assert updated_points == initial_points - 5


def test_do_not_update_club_points_if_purchase_is_ko(client):
    """
    Tests that club points are not deducted if the booking fails.
    :param client: The Flask test client.
    :return: None
    """
    initial_points = int([club for club in clubs if club["name"] == "Simply Lift"][0]["points"])
    result = client.post("/purchasePlaces", data={
        "competition": "Spring Festival",
        "club": "Simply Lift",
        "places": "25"
    })
    assert result.status_code == 200
    updated_points = int([club for club in clubs if club["name"] == "Simply Lift"][0]["points"])
    assert updated_points == initial_points


def test_update_competition_places_if_purchase_is_ok(client):
    """
    Tests that competitions places are correctly deducted after a successful booking.
    :param client: The Flask test client.
    :return: None
    """
    initial_places = int([competition for competition in competitions if competition["name"] == "Spring Festival"][0]["numberOfPlaces"])
    result = client.post("/purchasePlaces", data={
        "competition": "Spring Festival",
        "club": "Simply Lift",
        "places": "5"
    })
    assert result.status_code == 200
    assert 'Great-booking complete! You booked 5 places.' in result.data.decode()

    updated_places = int([competition for competition in competitions if competition["name"] == "Spring Festival"][0]["numberOfPlaces"])
    assert updated_places == initial_places - 5


def test_do_not_update_places_if_purchase_is_ko(client):
    """
    Tests that competitions places are not deducted if the booking fails.
    :param client: The Flask test client.
    :return: None
    """
    initial_places = int([competition for competition in competitions if competition["name"] == "Spring Festival"][0]["numberOfPlaces"])
    result = client.post("/purchasePlaces", data={
        "competition": "Spring Festival",
        "club": "Simply Lift",
        "places": "25"
    })
    assert result.status_code == 200
    updated_places = int([competition for competition in competitions if competition["name"] == "Spring Festival"][0]["numberOfPlaces"])
    assert updated_places == initial_places
