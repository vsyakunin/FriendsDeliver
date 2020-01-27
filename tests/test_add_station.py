import pytest
from webapp import app
import json
from webapp.model import db, User, Station, UserStation 
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

def test_handler_add_station_responses_200():
    test_data = {
        'station_id': 190,
        'weekday': 7
    }
    headers = {
        'Content-Type': 'application/json'
    }
    with app.test_client() as client:
        response = client.post('/v1/users/4/stations/', headers = headers, data=json.dumps(test_data))
    assert response.status == '200 OK'

    records = db.session.query(UserStation).filter(
        UserStation.user_id == 4, UserStation.station_id == 190
    ).all()

    assert len(records) == 1

def test_handler_add_station_responses_404():
    test_data = {
        'station_id': 182,
        'weekday': 7
    }
    headers = {
        'Content-Type': 'application/json'
    }
    with app.test_client() as client:
        response = client.post('/v1/users/-jbjbjnbk/stations/', headers = headers, data=json.dumps(test_data))
    assert response.status == '404 NOT FOUND'
