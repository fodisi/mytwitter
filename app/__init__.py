#!/usr/bin/env python3

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from .app_factory import ApplicationFactory

# Define the WSGI application object
# app = Flask(__name__)
# app.config.from_object('config')
app = ApplicationFactory.create_application('../config.py')
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Sample HTTP error handling


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


# Import a module / component using its blueprint handler variable (mod_auth)
from .auth.controller import authentication_ctrl as authentication
from .timeline.controller import timeline_ctrl as timeline
from .twit.controller import twit_ctrl as twit

# Register blueprint(s)
app.register_blueprint(authentication)
app.register_blueprint(timeline)
app.register_blueprint(twit)


# Build the database:
print('creating DB')
db.create_all()
