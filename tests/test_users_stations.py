import pytest
from webapp import app

def test_handler_users_stations_responses_200():
    with app.test_client() as client:
        response = client.get('/v1/stations/users/?from=35&to=66')
        assert response.status == '200 OK'
        json_data = response.get_json()
        assert len(json_data) > 0

def test_handler_users_stations_responses_404():
    with app.test_client() as client:
        response = client.get('/v1/stations/users/?from=-58&to=abcd')
        assert response.status == '404 NOT FOUND'

def test_handler_users_stations_returns_correct_structure():
    with app.test_client() as client:
        response = client.get('/v1/stations/users/?from=35&to=66')
        json_data = response.get_json()
        user = json_data[0]
        assert 'email' in user
        assert 'id' in user
        assert 'name' in user
