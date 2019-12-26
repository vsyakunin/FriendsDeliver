from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    
    def __repr__(self):
        return '<User {}>'.format(self.name)

class Station(db.Model):
    __tablename__ = 'stations'
    station_id = db.Column(db.Integer, primary_key=True)
    station_name = db.Column(db.String, nullable=False)
    active = db.Column(db.Boolean, nullable=False) 
    line_name = db.Column(db.String, nullable=False)
    line_id = db.Column(db.Integer, nullable=True)
    order_on_line = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return '<Station {}>'.format(self.station_name)      

class Line(db.Model):
    line_id = db.Column(db.Integer, primary_key=True)
    line_name = db.Column(db.String, nullable=False)
    color = db.Column(db.String, nullable=True) 

    def __repr__(self):
        return '<Line {}>'.format(self.line_name)     


users_stations = db.Table('users_stations',
    db.Column('user_id', db.Integer, db.ForeignKey('users.user_id')),
    db.Column('station_id', db.Integer, db.ForeignKey('stations.station_id')),
    db.PrimaryKeyConstraint('user_id', 'station_id', name='users_stations_primary_key'),
    db.Column('weekday', db.Integer, nullable=False)
)

stations_connections = db.Table('stations_connections',
    db.Column('from_id', db.Integer, db.ForeignKey('stations.station_id')),
    db.Column('to_id', db.Integer, db.ForeignKey('stations.station_id')),
    db.PrimaryKeyConstraint('from_id', 'to_id', name='stations_connections_primary_key')
)

