from http import HTTPStatus

from flask import Blueprint, request, jsonify
from .controllers import (
    create as create_post,
    get_all as get_all_posts
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
