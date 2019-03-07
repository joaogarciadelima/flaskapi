from flask import Blueprint, Flask

bp = Blueprint('users', __name__)


@bp.route('/<string:name>')
def user(name):
    return f'Hello {name}'


def init_app(app: Flask, url_prefix='/users'):
    app.register_blueprint(bp, url_prefix=url_prefix)
