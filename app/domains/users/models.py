import uuid
from sqlalchemy import func

from app.domains.posts.models import Post
from database import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(
        db.String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()))
    username = db.Column(db.String(20), nullable=False)
    created_at = db.Column(
        db.DateTime(timezone=True),
        server_default=func.now())
    profile = db.relationship(
        'Profile',
        back_populates='user',
        uselist=False
    )
    posts = db.relationship(
        Post, back_populates='user'
    )

    def serialize(self, detail=False):
        response = {
            'id': self.id,
            'username': self.username,
            'created_at': self.created_at
        }

        posts = []
        if self.posts:
            posts = [post.serialize() for post in self.posts]

        profile = None
        if self.profile:
            profile = self.profile.serialize()

        if detail:
            response.update({
                'profile': profile,
                'posts': posts
            })

        return response


class Profile(db.Model):
    __tablename__ = 'profiles'

    id = db.Column(
        db.String(36),
        db.ForeignKey('users.id'),
        primary_key=True
    )
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(40))
    birth_date = db.Column(db.DateTime(timezone=True))

    user = db.relationship(
        'User',
        back_populates='profile',
        uselist=False
    )

    def serialize(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'birth_date': datetime.strftime(self.birth_date, '%Y-%m-%d')
        }