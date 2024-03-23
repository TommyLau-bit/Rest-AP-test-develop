from sqlalchemy import Integer, String, ForeignKey, Column
from sqlalchemy.orm import relationship
from . import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    # Relationships
    cases = relationship('Case', backref='user')
    complaints = relationship('Complaint', backref='user')

class Case(db.Model):
    __tablename__ = 'case'
    id = db.Column(db.Integer, primary_key=True)
    case_type = db.Column(db.String, nullable=False)
    status = db.Column(db.String, nullable=False)
    request_received_year = db.Column(db.String)
    request_received_month = db.Column(db.String)
    request_closed_year = db.Column(db.String)
    request_closed_month = db.Column(db.String)
    user_id = db.Column(db.ForeignKey('user.id'))

class Complaint(db.Model):
    __tablename__ = 'complaint'
    id = db.Column(db.Integer, primary_key=True)
    reason_grouped = db.Column(db.String)
    user_id = db.Column(db.ForeignKey('user.id'))

class Dashboard(db.Model):
    __tablename__ = 'dashboard'
    id = db.Column(db.Integer, primary_key=True)
    active_days = db.Column(db.String)
    closed_on_time = db.Column(db.String)
    case_active_grouped = db.Column(db.String)
    user_id = db.Column(db.ForeignKey('user.id'))

class Filter(db.Model):
    __tablename__ = 'filter'
    id = db.Column(db.Integer, primary_key=True)
    criteria = db.Column(db.String)
    user_id = db.Column(db.ForeignKey('user.id'))
