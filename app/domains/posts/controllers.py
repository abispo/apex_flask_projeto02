from app.domains.posts.models import Post
from database.actions import save


def create(data):
    user_id = data.get('user_id')
    title = data.get('title')
    text = data.get('text')

    post = Post(
        user_id=user_id,
        title=title,
        text=text
    )

    return save(post)


def get_all():
    return Post.query.all()
