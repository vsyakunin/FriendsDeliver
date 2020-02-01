import pytest
from webapp import app

def test_handler_station_responses_200():
    with app.test_client() as client:
        response = client.get('/v1/stations/')
        assert response.status == '200 OK'
        json_data = response.get_json()
        assert len(json_data) > 0

def test_handler_station_returns_correct_structure():
    with app.test_client() as client:
        response = client.get('/v1/stations/')
        json_data = response.get_json()
        station = json_data[0]
        assert 'active' in station
        assert 'id' in station
        assert 'line_id' in station
        assert 'name' in station
        assert 'order_on_line' in station
