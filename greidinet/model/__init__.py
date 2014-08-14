# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function, unicode_literals)
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from datetime import datetime

class Entry(db.Model):
    """Represents a climbed route."""
    # id 
    id = db.Column(db.Integer, primary_key=True)
    # user
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User',
            backref=db.backref('entries', lazy='dynamic'))    
    # route
    route_id = db.Column(db.Integer, db.ForeignKey('route.id'))
    route = db.relationship('Route',
            backref=db.backref('entries', lazy='dynamic'))

    def __init__(self, user, route):
        self.route = route
        self.user = user

    def __repr__(self):
        return '<Entry %s : %s>' % (self.user, self.route)

class User(db.Model):
    """Represents a climber."""
    # id
    id = db.Column(db.Integer, primary_key=True)
    # username
    username = db.Column(db.String(256), unique=True)
    # full name
    name = db.Column(db.String(2048))

    def __init__(self, username, name):
        self.username = username
        self.name = name

    def __repr__(self):
        return '<User %r>' % self.username

class Route(db.Model):
    """Represents a single route."""
    # id
    id = db.Column(db.Integer, primary_key=True)
    # name
    name = db.Column(db.String(2048))
    # grade
    grade_id = db.Column(db.Integer, db.ForeignKey('grade.id'))
    grade = db.relationship('Grade',
            backref=db.backref('routes', lazy='dynamic'))
    # location
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'))
    location = db.relationship('Location',
            backref=db.backref('routes', lazy='dynamic'))

    def __init__(self, name, location, sector=None):
        self.name = name
        self.location = location

    def __repr__(self):
        return '<Route %r on %r>' % (self.name, self.location)

class Location(db.Model):
    """Represents a climbing location: crag, mountain, gym, etc."""
    # id
    id = db.Column(db.Integer, primary_key=True)
    # name
    name = db.Column(db.String(2048), unique=True)
    # category
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category',
            backref=db.backref('locations', lazy='dynamic'))
    
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def __repr__(self):
        return '<Location %r (%r)>' % (self.name, self.category)

class Category(db.Model):
    """Represents a type of location: crag, mountain, gym, etc."""
    # id
    id = db.Column(db.Integer, primary_key=True)
    # name
    name = db.Column(db.String(2048), unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Category %r>' % self.name

class Grade(db.Model):
    """Represents a climbing grade, eg. 7A, 5+, or 5.10."""
    # id
    id = db.Column(db.Integer, primary_key=True)
    # name
    name = db.Column(db.String(128), unique=True)
    # grade type
    gradetype_id = db.Column(db.Integer, db.ForeignKey('gradetype.id'))
    gradetype = db.relationship('GradeType'
            backref=db.backref('grades', lazy='dynamic'))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Grade %r>' % self.name

class GradeType(db.Model):
    """Represents a type of a grade, eg. UK trad., Finnish sport, or similar."""
    # id 
    id = db.Column(db.Integer, primary_key=True)
    # name
    name = db.Column(db.String(2048), unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<GradeType %r>' % self.name
