# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function, unicode_literals)
from flask import Blueprint, abort, render_template
from jinja2 import TemplateNotFound
from flask.ext.login import LoginManager, UserMixin, AnonymousUserMixin
from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, HiddenField, ValidationError, SubmitField, FormField, BooleanField, validators
from wtforms.validators import Required, Optional
from greidinet.model import db, User

login_manager = LoginManager()

class LoginUser(User, UserMixin):
    def is_active(self):
        return self.active
    
    def get_id(self):
        return self.username

@login_manager.user_loader
def load_user(username):
    user = LoginUser.query.filter_by(username=username).first()
    return user

class LoginForm(Form):
    username = StringField(u'Username', validators=[Required()])
    password = PasswordField(u'Password', validators=[Required()])
    remember = BooleanField(u'Remember me', default=False)
    submit = SubmitField(u'Log in')


logingui = Blueprint('logingui', __name__)

@logingui.route('/login')
def login():
    form = LoginForm()
    if (form.validate_on_submit()):
        # Login and validate the user
        abort(501) 
    try:
        return render_template('login.html', form=form)
    except TemplateNotFound:
        abort(501)

    
