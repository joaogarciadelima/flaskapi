from flask import Flask

from blueprints.users import bp as usuarios_bp

from blueprints.base import bp as base_bp


def create_app():
    app = Flask(__name__)


    # Blueprints
    usuarios_bp.init_app(app)
    usuarios_bp.init_app(app, '/usuarios')

    base_bp.init_app(app)

    return app