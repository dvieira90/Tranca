from flask import Blueprint

homepage = Blueprint('homepage', __name__)


@homepage.route('/')
def home():
    return 'helloo'
