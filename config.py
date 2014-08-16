# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function, unicode_literals)

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = "df2x1aqw%~6&y8k4@!U-Hj8e8*5&)58_t(@9wYc%*+847P90uxNh2ewf3"
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp//gredinet.db'

class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost'

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
