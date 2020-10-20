from app.domains.users.exceptions import UserProfileNotFoundError
from app.domains.users.models import User, Profile
from database.actions import save, delete
from datetime import datetime

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


def create_profile(id, data):
    user = get_by_id(id)
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    birth_date = datetime.strptime(
        data.get('birth_date'), '%Y-%m-%d'
    )

    profile = Profile(
        first_name=first_name,
        last_name=last_name,
        birth_date=birth_date
    )

    user.profile = profile
    save(user)
    return user.profile


def get_profile_by_user_id(id):
    user = get_by_id(id)
    if not user.profile:
        raise UserProfileNotFoundError

    return user.profile
