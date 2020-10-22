from app.domains.categories.models import Category
from database.actions import save


def get():
    return Category.query.all()


def create(data):
    name = data.get('name')

    category = Category(name=name)
    return save(category)
