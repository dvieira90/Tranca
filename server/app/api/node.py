from flask import Blueprint

node = Blueprint('node', __name__)


@node.route('/api')
def api():
    return 'helloo'
