#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)

from .api import api
app.register_blueprint(api)
