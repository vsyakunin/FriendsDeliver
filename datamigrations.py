import os
from pathlib import Path
import webapp 
from webapp.model import db, User, Station, Line
import json
from flask_sqlalchemy import SQLAlchemy
from webapp.__init__ import create_app

app = create_app()
app.app_context().push()

basedir = os.path.abspath(os.path.dirname(__file__))
data_dir = os.path.join(basedir, 'webapp', 'datamigrations')
files_list = []
all_data = []
file_model_pairs = {}
for file in os.listdir(data_dir):
    if file.endswith('.json'):
        files_list.append(file)

def save_data(model_name, needed_data):
    new_data = model_name(**needed_data)
    db.session.add(new_data)
    db.session.commit()

for file in files_list:
    data_folder = Path('webapp/datamigrations/')
    file_to_open = data_folder / file
    file_name = file.replace('.json','')
    with open(file_to_open, 'r', encoding='cp1251') as f:
        all_data.append(json.load(f))
        file_model_pairs[file_name] = str(file_name).capitalize()[:-1]

for i in range (len(all_data)):
    model_name = list(file_model_pairs.values())[i]
    model_name = eval(model_name)
    data_to_save = all_data[i]
    
    for k in range (len(data_to_save)):
        needed_data = data_to_save[k]
        save_data(model_name, needed_data)

    


