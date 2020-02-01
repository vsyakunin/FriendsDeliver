import pytest
import json
from flask_sqlalchemy import SQLAlchemy
from webapp.model import db, User, Station, UserStation
from webapp import create_app

@pytest.fixture
def app():
    app = create_app()
    return app

# @pytest.fixture()
# def init_database():
#     db.create_all()
 
#     user_station_1 = UserStation(user_id=1, station_id=1, weekday=1)
#     db.session.add(user_station_1)

#     user_1 = User(id=1, name='George', email='george.bluth@reqres.in', password='123', delivers=True)
#     db.session.add(user_1)

#     station_1 = Station(id=1, name='Новокосино', active=True, line_id=1, order_on_line=1)
#     db.session.add(station_1)

#     db.session.commit()
 
#     yield db
 
#     db.drop_all()

