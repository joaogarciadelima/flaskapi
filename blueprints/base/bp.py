from flask import Blueprint, Flask

bp = Blueprint('base', __name__)

@bp.route('/')
def hello():
    return 'Hello World!'


def init_app(app: Flask, url_prefix=''):
    app.register_blueprint(bp)