from flask import Flask
from flask_migrate import Migrate

from api import db, api

def create_app():
    app = Flask(__name__)
    configure_app(app)
    api.init_app(app)
    migrate = Migrate()
    db.init_app(app)
    migrate = Migrate(app, db)

    return app

def configure_app(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://api:example@localhost/api"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
