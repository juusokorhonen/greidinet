# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function, unicode_literals)
from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.appconfig import AppConfig

def create_app(configfile=None):
    app = Flask(__name__)
    # Configure app
    AppConfig(app, configfile)
    # Use Bootstrap
    Bootstrap(app)
    # Import blueprints
    
    return app
