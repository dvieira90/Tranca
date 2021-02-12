#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)
app.secret_key = 'alura'


if __name__ == '__main__':
    app.run(debug=True, host='localhost')
