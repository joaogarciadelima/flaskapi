from flask import Blueprint, Flask

from blueprints.users.models import User
from ext.db import db


bp = Blueprint('users', __name__)


@bp.route('/<string:name>')
def user(name):
    user = User(name=name)
    db.session.add(user)
    db.session.commit()
    return f'Hello {user}'


@bp.route('/listar')
def listar():
    users = User.query.order_by(User.name).all()
    return str(users)


def init_app(app: Flask, url_prefix='/users'):
    app.register_blueprint(bp, url_prefix=url_prefix)
