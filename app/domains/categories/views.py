from http import HTTPStatus

from flask import Blueprint, jsonify, request

from .controllers import (
    get as get_all_categories,
    create as create_category
)

categories_app = Blueprint(
    'app.categories',
    __name__,
    url_prefix='/categories'
)


@categories_app.route('', methods=['GET'])
def get():
    return jsonify([
        category.serialize() for category in get_all_categories()
    ]), HTTPStatus.OK


@categories_app.route('', methods=['POST'])
def post():
    data = request.get_json()
    category = create_category(data)
    return jsonify(category.serialize()), HTTPStatus.CREATED

