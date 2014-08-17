# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function, unicode_literals)
from flask import Blueprint, abort, render_template
from jinja2 import TemplateNotFound
from greidinet.login import LoginForm

simplegui = Blueprint(u'simplegui', __name__)

@simplegui.route('/')
def frontpage():
    try:
        loginform=LoginForm()
        return render_template('index.html', loginform=loginform)
    except TemplateNotFound:
        abort(501)
