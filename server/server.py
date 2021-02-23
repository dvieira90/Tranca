#!/usr/bin/python3
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'

db = SQLAlchemy(app)

# Classes do banco


class Users(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    login = db.Column(db.String(100))

    def __init__(self, login):
        self.login = login


class Tags(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100))
    tag = db.Column(db.String(20))

    def __init__(self, nome, tag):
        self.nome = nome
        self.tag = tag


class Portas(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100))


class Portas_Users():
    portas_id = db.Column(db.Integer, db.ForeignKey(
        'portas.id'), nullable=False)
    users_id = db.Column(db.Integer, db.ForeignKey(
        'users.id'), nullable=False)


class User_Tags():
    tags_id = db.Column(db.Integer, db.ForeignKey(
        'tags.id'), nullable=False)
    users_id = db.Column(db.Integer, db.ForeignKey(
        'users.id'), nullable=False)

# Rotas


@app.route("/")
def hello_world():
    return render_template('index.html', message='Teste')


# Main
if __name__ == '__main__':
    app.run(debug=True)
