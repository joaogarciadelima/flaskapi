from os import path

SQLALCHEMY_TRACK_MODIFICATIONS = False

_dirname = path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = f'sqlite:///{_dirname}/db.sqlite3'
