import pytest


def test_show_competitions_details(client):
    result = client.post("/showSummary", data={"email": "john@simplylift.co"})
    assert result.status_code == 200
    assert 'Spring Festival' in result.data.decode()
    assert 'Number of Places: 25' in result.data.decode()
    expected_url = "/book/Spring%20Festival/Simply%20Lift"
    assert f'href="{expected_url}"' in result.data.decode()
