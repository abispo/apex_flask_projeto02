import json

from flask import Flask
from werkzeug.exceptions import HTTPException

from app.domains.categories.views import categories_app
from app.domains.files.views import files_app
from database import db, migrate

from app.domains.users.views import users_app
from app.domains.posts.views import posts_app


def create_app():
    app = Flask(__name__)

    app.config.from_object('settings')
    db.init_app(app)
    migrate.init_app(app, db)

    _register_blueprints(app)

    app.register_error_handler(
        HTTPException, _handle_default_exception
    )

    return app


def _handle_default_exception(e):
    response = e.get_response()
    code = e.code
    description = e.description

    response.data = json.dumps({
        'code': code,
        'description': description
    })

    response.content_type = 'application/json'
    return response.data, code


def _register_blueprints(app):
    app.register_blueprint(users_app, url_prefix='/users')
    app.register_blueprint(posts_app, url_prefix='/posts')
    app.register_blueprint(categories_app)
    app.register_blueprint(files_app)
