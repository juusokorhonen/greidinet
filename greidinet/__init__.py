# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function, unicode_literals)
from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.appconfig import AppConfig

def create_app(configfile=None, default_settings=True):
    app = Flask(__name__)
    # Configure app
    AppConfig(app, configfile=configfile, default_settings=default_settings)
    # Open db model
    from greidinet.model import db
    db.init_app(app)
    # DEBUG
    if (app.debug):
        app.test_request_context().push()
        db.drop_all()
        db.create_all()
    # Use Bootstrap
    Bootstrap(app)
    # Login module
    from greidinet.login import login_manager, logingui
    login_manager.init_app(app)
    app.register_blueprint(logingui)
    # REST api
    from greidinet.restapi import restapi
    restapi.init_app(app, flask_sqlalchemy_db=db)
    restapi.create_apis()
    # Import blueprints
    from greidinet.simplegui import simplegui
    app.register_blueprint(simplegui)
   

    return app
