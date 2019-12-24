import os
from pathlib import Path
import webapp 
from webapp.model import db, User, Station, Line
import json
from flask_sqlalchemy import SQLAlchemy
from webapp.__init__ import create_app

app = create_app()
app.app_context().push()

files_list = []
for file in os.listdir('C:\projects\FriendsDeliver\webapp\datamigrations'):
    if file.endswith('.json'):
        files_list.append(file)

def save_user(name, email, password):
    user_exists = User.query.filter(User.email == email).count()
    if not user_exists:
        new_user = User(name=name, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        
def save_station(station_name, active, line_name):
    new_station = Station(station_name=station_name, active=active, line_name=line_name)
    db.session.add(new_station)
    db.session.commit()

def save_line(line_name):
    line_exists = Line.query.filter(Line.line == line_name).count()
    if not line_exists:
        new_line = Line(line=line_name)
        db.session.add(new_line)
        db.session.commit()

if 'users.json' in files_list:
    data_folder = Path('webapp/datamigrations/')
    file_to_open = data_folder / 'users.json'
    with open(file_to_open, 'r', encoding='utf-8') as f:
        users = json.load(f)
        for user in users:
            name=user['name']
            email=user['email']
            password=user['password']
            save_user(name, email, password)

if 'stations.json' in files_list:
    data_folder = Path('webapp/datamigrations/')
    file_to_open = data_folder / 'stations.json'
    with open(file_to_open, 'r', encoding='cp1251') as f:
        stations = json.load(f)
        for station in stations:
            station_name=station['Station']
            status=station['Status']
            if status=='действует':
                active=True
            else:
                active=False      
            line_name=station['Line']
            save_station(station_name, active, line_name)
            save_line(line_name)
            



