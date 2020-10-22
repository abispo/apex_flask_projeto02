import uuid

from app.domains.posts.models import posts_categories
from database import db


class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(
        db.String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )
    name = db.Column(
        db.String(30), nullable=False
    )

    posts = db.relationship(
        'Post',
        secondary=posts_categories)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }
