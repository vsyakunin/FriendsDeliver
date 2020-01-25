from flask import Flask, Response, jsonify, request, abort
from webapp.model import db, User, Station, UserStation 
from marshmallow import Schema, fields

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    return app  

app = create_app()

class UserSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    email = fields.Str()
    
class StationSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    active = fields.Boolean()
    line_id = fields.Int()
    order_on_line = fields.Int()

def user_exists(user_id):
    users_list = User.query.filter(User.id == user_id).all()
    return len(users_list)>0

def station_exists(station_id):
    stations_list = Station.query.filter(Station.id == station_id).all()
    return len(stations_list)>0

@app.route('/hi')
def index():
    return 'hi'

@app.route('/v1/stations/')
def stations():    
    stations_list = Station.query.all()
    schema = StationSchema(many=True)
    result = schema.dump(stations_list)
    return jsonify(result)

@app.route('/v1/stations/users/')
def users_stations():
    station_from = request.args.get('from', type = int)
    if not station_exists(station_from):
        abort(404)
    station_to = request.args.get('to', type = int)
    if not station_exists(station_to):
        abort(404)
    users_from = User.query.join(
        UserStation, 
        User.id == UserStation.user_id
    ).filter(
        UserStation.station_id == station_from
    )
    
    users_to = User.query.join(
        UserStation, 
        User.id == UserStation.user_id
    ).filter(
        UserStation.station_id == station_to
    )

    users_list = users_from.join(users_to).all()
    
    schema = UserSchema(many = True)
    result = schema.dump(users_list)
    return jsonify(result)

@app.route('/v1/users/<user_id>/stations/') 
def get_station(user_id):
    if not user_exists(user_id):
        abort(404)
    users_stations = Station.query.join(
        UserStation, 
        Station.id == UserStation.station_id
    ).filter(
        UserStation.user_id == user_id
    ).all()

    schema = StationSchema(many = True)
    result = schema.dump(users_stations)
    return jsonify(result)    

@app.route('/v1/users/<user_id>/stations/', methods=['POST']) 
def add_station(user_id):
    if not user_exists(user_id):
        abort(404)
    json_data = request.json
    station_id = json_data['station_id']
    weekday = json_data['weekday']

    user_station = UserStation(user_id=user_id, station_id=station_id, weekday=weekday)
    db.session.add(user_station)
    db.session.commit()
    return jsonify(['record successfully added'])

@app.route('/v1/users/<user_id>/stations/<station_id>/', methods=['DELETE']) 
def delete_station(user_id, station_id):
    if not user_exists(user_id):
        abort(404)
    if not station_exists(station_id):
        abort(404)
    record_to_delete = UserStation.query.filter(
        UserStation.user_id == user_id, 
        UserStation.station_id==station_id
    ).first()
    db.session.delete(record_to_delete)
    db.session.commit()
    return jsonify(['record succesfully deleted'])
