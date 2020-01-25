import json
from pathlib import Path
import os

basedir = os.path.abspath(os.path.dirname(__file__))
data_dir = os.path.join(basedir, 'webapp', 'datamigrations')

users_stations = {}
us=users_stations
print('users id:')
us["user_id"]=int(input())
print('stations id:')
us["station_id"]=int(input())
print('weekday:')
us["weekday"]=int(input())

def append_record(record):
    data_folder = Path('webapp/datamigrations/')
    file_name = 'users_stations.json'
    file_to_open = data_folder / file_name
    with open(file_to_open, 'r+', encoding='utf-8') as f:
        f.seek(0,2)
        position = f.tell() -1
        f.seek(position)
        f.write( ",{}]".format(json.dumps(record)))

append_record(us)

