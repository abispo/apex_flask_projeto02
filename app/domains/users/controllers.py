from app.domains.users.models import User
from database.actions import save, delete


def create(data):
    username = data.get('username')
    user = User(username=username)
    return save(user)


def get_all():
    return User.query.all()


def get_by_id(id):
    return User.query.get(id)


def update(id, data):
    user = get_by_id(id)
    username = data.get('username')

    user.username = username
    return save(user)


def remove(id):
    user = get_by_id(id)
    delete(user)
