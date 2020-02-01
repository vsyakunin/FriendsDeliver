import pytest
from webapp import app
import json
from webapp.model import db, User, Station, UserStation 
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

def test_handler_delete_station_responses_200():
    headers = {
        'Content-Type': 'application/json'
    }
    with app.test_client() as client:
        response = client.delete('/v1/users/4/stations/190/', headers = headers)
    assert response.status == '200 OK'

    records = db.session.query(UserStation).filter(
        UserStation.user_id == 4, UserStation.station_id == 190
    ).all()

    assert len(records) == 0

def test_handler_delete_station_responses_404():
    headers = {
        'Content-Type': 'application/json'
    }
    with app.test_client() as client:
        response = client.delete('/v1/users/-iehuise/stations/0/', headers = headers)
    assert response.status == '404 NOT FOUND'
