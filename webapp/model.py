from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.orm import relationship, backref

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    delivers = db.Column(db.Boolean, nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def __repr__(self):
        return '<User {}>'.format(self.name)

class Station(db.Model):
    __tablename__ = 'stations'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    active = db.Column(db.Boolean, nullable=False) 
    line_id = db.Column(db.Integer, db.ForeignKey('lines.id'))
    line = relationship('Line', backref=backref('lines'))
    order_on_line = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return '<Station {}>'.format(self.name)

class Line(db.Model):
    __tablename__ = 'lines'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    color = db.Column(db.String, nullable=True) 

    def __repr__(self):
        return '<Line {}>'.format(self.line_name)

class UserStation(db.Model):
    __tablename__ = 'users_stations'
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    station_id = db.Column(db.Integer, db.ForeignKey('stations.id'))
    weekday = db.Column(db.Integer, nullable=False)
    __table_args__ = (
        db.PrimaryKeyConstraint('user_id', 'station_id', 'weekday', name='users_stations_primary_key'),)
    
stations_connections = db.Table('stations_connections',
    db.Column('from_id', db.Integer, db.ForeignKey('stations.id')),
    db.Column('to_id', db.Integer, db.ForeignKey('stations.id')),
    db.PrimaryKeyConstraint('from_id', 'to_id', name='stations_connections_primary_key')
)

