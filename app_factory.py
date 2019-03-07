from flask import Flask

import settings as default_settings
from blueprints.users import bp as usuarios_bp
from blueprints.base import bp as base_bp
from ext import migrate
from ext.db import db


def create_app(settings=None) -> Flask:
    app = Flask(__name__)
    if settings == None:
        settings = default_settings

    app.config.from_object(settings)

    # Extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Blueprints
    usuarios_bp.init_app(app)
    usuarios_bp.init_app(app, '/usuarios')

    base_bp.init_app(app)

    return app
