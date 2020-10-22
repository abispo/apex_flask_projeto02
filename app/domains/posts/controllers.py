from app.domains.categories.models import Category
from app.domains.posts.models import Post
from database.actions import save


def create(data):
    user_id = data.get('user_id')
    title = data.get('title')
    text = data.get('text')

    categories_ids = data.get('categories')
    categories_list = [Category.query.get(id) for id in categories_ids]

    post = Post(
        user_id=user_id,
        title=title,
        text=text
    )

    post.categories = categories_list

    return save(post)


def get_all():
    return Post.query.all()


def get_by_id(id):
    return Post.query.get(id)


def get_all_categories_by_id(id):
    return Post.query.get(id).categories


def create_category_by_post_id(id, data):
    category_name = data.get('name')
    category = Category(name=category_name)

    post = Post.query.get(id)
    post.categories.append(category)

    save(post)
    return category
