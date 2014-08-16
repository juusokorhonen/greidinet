# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function, unicode_literals)
from flask import Flask, Blueprint, current_app, url_for
from flask.ext.restless import APIManager
import types
from greidinet.model import *

restapi = APIManager()

# Dynamically bind create_apis() method to the APIManager class (there probably should be a nicer way to accomplish this)

def create_apis(self):
    self.create_api(GradeType, methods=['GET', 'POST', 'DELETE', 'PATCH'])
    self.create_api(Grade)
    self.create_api(Category)
    self.create_api(Location)
    self.create_api(Route)
    self.create_api(User)
    self.create_api(Entry)

restapi.create_apis = types.MethodType(create_apis, restapi, restapi.__class__)
