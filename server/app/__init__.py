#!/usr/bin/python3
from .pages.homepage import homepage
from .api.node import node
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'

db = SQLAlchemy(app)


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


app.register_blueprint(homepage)
app.register_blueprint(node)
