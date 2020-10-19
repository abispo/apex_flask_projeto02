from app.domains.users.models import User
from database.actions import save


def create_user(data):
    username = data.get('username')
    user = User(username=username)
    return save(user)


def get_all():
    return User.query.all()