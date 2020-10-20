from http import HTTPStatus

from flask import Blueprint, jsonify, request
from app.domains.users.controllers import (
    get_all,
    create as create_user,
    get_by_id as get_user_by_id,
    update as update_user,
    remove as remove_user,
    create_profile as create_user_profile,
    get_profile_by_user_id
)

users_app = Blueprint('app.users', __name__)


@users_app.route('', methods=['GET'])
def get():
    return jsonify([user.serialize() for user in get_all()]), HTTPStatus.OK


@users_app.route('', methods=['POST'])
def post():
    data = request.get_json()
    user = create_user(data)

    return jsonify(user.serialize()), HTTPStatus.CREATED


@users_app.route('<id>', methods=['GET'])
def get_by_id(id):
    user = get_user_by_id(id)
    return jsonify(user.serialize(detail=True)), HTTPStatus.OK


@users_app.route('<id>', methods=['PATCH'])
def patch(id):
    data = request.get_json()
    user = update_user(id, data)

    return jsonify(user.serialize()), HTTPStatus.NO_CONTENT


@users_app.route('<id>', methods=['DELETE'])
def delete(id):
    remove_user(id)
    return jsonify(), HTTPStatus.NO_CONTENT


@users_app.route('<id>/profile', methods=['POST'])
def post_profile(id):
    data = request.get_json()
    profile = create_user_profile(id, data)
    return jsonify(profile.serialize()), HTTPStatus.CREATED


@users_app.route('<id>/profile', methods=['GET'])
def get_profile_by_id(id):
    profile = get_profile_by_user_id(id)
    return jsonify(profile.serialize()), HTTPStatus.OK
