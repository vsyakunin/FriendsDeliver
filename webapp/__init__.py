from flask import Flask, Response, jsonify
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
    users_list = User.query.join(
        UserStation, 
        User.id == UserStation.user_id
    ).filter(
        UserStation.station_id == 167
    ).all()
    schema = UserSchema(many = True)
    result = schema.dump(users_list)
    return jsonify(result)
    
    





