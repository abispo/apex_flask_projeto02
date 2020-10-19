
from flask import Flask
from database import db, migrate

from app.domains.users.views import users_app


def create_app():
    app = Flask(__name__)

    app.config.from_object('settings')
    db.init_app(app)
    migrate.init_app(app, db)

    _register_blueprints(app)

    return app


def _register_blueprints(app):
    app.register_blueprint(users_app, url_prefix='/users')