#!/usr/bin/python3
from ..server import app


@app.route('/', methods=['GET', ])
def urls():
    return "Teste"
