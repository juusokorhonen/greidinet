# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function, unicode_literals)
from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.appconfig import AppConfig

def create_app(configfile=None):
    app = Flask(__name__)
    # Configure app
    AppConfig(app, configfile)
    # Open db model
    from greidinet.model import db
    db.init_app(app)
    # DEBUG
    app.test_request_context().push()
    db.drop_all()
    db.create_all()
    # Use Bootstrap
    Bootstrap(app)
    # Import blueprints
    #from greidinet.simplegui import simplegui
    #app.register_blueprint(simplegui)
    # REST api
    from greidinet.restapi import restapi
    restapi.init_app(app, flask_sqlalchemy_db=db)
    restapi.create_apis()
    

    return app
