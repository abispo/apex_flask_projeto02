from http import HTTPStatus

from flask import Blueprint, request, jsonify
from .controllers import (
    create as create_post,
    get_all as get_all_posts,
    get_by_id as get_post_by_id,
    get_all_categories_by_id as get_all_post_categories_by_id,
    create_category_by_post_id
)

posts_app = Blueprint('app.posts', __name__)


@posts_app.route('', methods=['POST'])
def post():
    data = request.get_json()
    post = create_post(data)

    return jsonify(post.serialize()), HTTPStatus.CREATED


@posts_app.route('', methods=['GET'])
def get():
    return jsonify([
        post.serialize() for post in get_all_posts()
    ])


@posts_app.route('<id>', methods=['GET'])
def get_by_id(id):
    post = get_post_by_id(id)
    return jsonify(post.serialize(detail=True))


@posts_app.route('<id>/categories', methods=['GET'])
def get_post_categories(id):
    categories = [
        category.serialize() for category in get_all_post_categories_by_id(id)
    ]

    return jsonify(categories), 200


@posts_app.route('<id>/categories', methods=['POST'])
def create_category(id):
    data = request.get_json()
    category = create_category_by_post_id(id, data)

    return jsonify(category.serialize()), HTTPStatus.CREATED
