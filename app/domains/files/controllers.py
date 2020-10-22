import os

from werkzeug.utils import secure_filename

from database.actions import save
from settings import UPLOAD_FOLDER
from .models import File


def create(filename):
    file = File(name=filename)

    return save(file)


def get():
    return File.query.all()


def upload_file(_file):
    filename = secure_filename(_file.filename)
    _file.save(os.path.join(UPLOAD_FOLDER, filename))

    return create(filename)

