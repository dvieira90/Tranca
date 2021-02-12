#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)


from .api.node import node
from .pages.homepage import homepage

app.register_blueprint(homepage)
app.register_blueprint(node)
