from app import db
from datetime import datetime

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    firstname = db.Column(db.String(64))
    lastname = db.Column(db.String(64))
    city = db.Column(db.String(64))
    state = db.Column(db.String(64))
    country = db.Column(db.String(64))
    bio = db.Column(db.String(250))
    cohort = db.Column(db.String(64))
    linkedin = db.Column(db.String(64))


class TimePreference(db.Model):
    id = db.Column(db.Integer, primary_key=True)


class