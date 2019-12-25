import os
import json
import requests

STATION_URL = 'https://api.hh.ru/metro/1'
USER_URL = 'https://reqres.in/api/users/'

def save_to_json(filename, data):
    json_file = os.path.join(os.path.dirname(__file__), 'datamigrations', filename + '.json')
    with open(json_file, 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False)

def get_station(url):
    stations = []
    response = requests.get(url)
    lines = response.json()['lines']
    for line in lines:
        for s in line['stations']:
            stations.append({'station_name':s['name'], 'order':s['order'], 'active':True, 'line':line['name']})

    save_to_json('stations', stations)

def get_test_users(url):
    users = []
    for i in range(1,13):
        response = requests.get(url + str(i))
        user = response.json()['data']
        users.append({'name':user['first_name'], 'email':user['email'], 'password':user['last_name'] + str(user['id'])})

    save_to_json('users', users)
