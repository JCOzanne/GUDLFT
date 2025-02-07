def test_club_points_update_after_booking(client, monkeypatch):
    test_clubs = [
        {"name": "Simply Lift", "email": "john@simplylift.co", "points": "20"},
        {"name": "Iron Temple", "email": "admin@irontemple.com", "points": "4"}
    ]
    test_competitions = [
        {"name": "Spring Festival", "date": "2030-03-27 10:00:00", "numberOfPlaces": "25"}
    ]

    monkeypatch.setattr('server.clubs', test_clubs)
    monkeypatch.setattr('server.competitions', test_competitions)

    client.post("/purchasePlaces", data={
        "competition": "Spring Festival",
        "club": "Simply Lift",
        "places": "5"
    })

    response = client.get("/clubPoints")
    assert response.status_code == 200
    assert "Simply Lift" in response.data.decode()
    assert "8" in response.data.decode()