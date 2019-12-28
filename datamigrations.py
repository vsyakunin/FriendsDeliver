import os
from pathlib import Path
import webapp 
from webapp.model import db, User, Station, Line
import json
from flask_sqlalchemy import SQLAlchemy
from webapp.__init__ import create_app

app = create_app()
app.app_context().push()

MODELS_MAP = {
    'users.json': User,
    'stations.json': Station,
    'lines.json': Line
}

basedir = os.path.abspath(os.path.dirname(__file__))
data_dir = os.path.join(basedir, 'webapp', 'datamigrations')
files_list = []
all_data = {}

for item in os.listdir(data_dir):
    if item.endswith('.json'):
        files_list.append(item)

def save_data(current_model, record):
    new_record = current_model(**record)
    db.session.add(new_record)
    db.session.commit()

for file_name in files_list:
    data_folder = Path('webapp/datamigrations/')
    file_to_open = data_folder / file_name
    with open(file_to_open, 'r', encoding='utf-8') as f:
        for record in json.load(f):
            current_model = (MODELS_MAP[file_name])
            save_data(current_model, record)
