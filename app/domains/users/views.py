from http import HTTPStatus

from flask import Blueprint, jsonify
from app.domains.users.controllers import get_all

users_app = Blueprint('app.users', __name__)


@users_app.route('', methods=['GET'])
def get_all_users():
    return jsonify([user.serialize() for user in get_all()]), HTTPStatus.OK
