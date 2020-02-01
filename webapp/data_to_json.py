import os
import json
import requests
from werkzeug.security import generate_password_hash


STATION_URL = 'https://api.hh.ru/metro/1'
USER_URL = 'https://reqres.in/api/users/'
ROOT_DIR = os.path.join(os.path.dirname(__file__), 'datamigrations')

def save_to_json(filename, data):
    json_file = os.path.join(ROOT_DIR, filename + '.json')
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)

def get_stations(url):
    stations = []
    lines = []
    response = requests.get(url)
    items = response.json()['lines']
    for line in items:
        lines.append({'id': line['id'], 'name': line['name'], 'color': line['hex_color']})
        for s in line['stations']:
            stations.append({'name': s['name'], 'active': True, 'line_id': line['id'],
                            'order_on_line': s['order']})

    save_to_json('lines', lines)
    save_to_json('stations', stations)

def get_test_users(url):
    users = []
    for i in range(1,13):
        response = requests.get(url + str(i))
        user = response.json()['data']
        hash_pass = generate_password_hash(user['last_name'] + str(user['id']))
        users.append({'name': user['first_name'], 'email': user['email'],
                    'password': hash_pass, 'delivers': True})

    save_to_json('users', users)

get_stations(STATION_URL)
get_test_users(USER_URL)
