from . import api

@api.route('/')
def home():
    return 'helloo'