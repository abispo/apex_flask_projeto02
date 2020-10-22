from flask import Blueprint, jsonify, request
from flask.views import MethodView

from .controllers import (
    create as create_file_info,
    get as get_files_information, upload_file
)

files_app = Blueprint('app.files', __name__)


class FileAPI(MethodView):

    def get(self):
        return jsonify([
            file.serialize() for file in get_files_information()
        ])

    def post(self):
        _file = request.files.get('file')
        file = upload_file(_file)

        return jsonify(file.serialize()), 201


file_view = FileAPI.as_view('file_api_view')
files_app.add_url_rule(
    '/files', view_func=file_view, methods=['GET']
)
files_app.add_url_rule(
    '/files', view_func=file_view, methods=['POST']
)
