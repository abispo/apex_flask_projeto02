import uuid
from sqlalchemy import func
from database import db


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

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'created_at': self.created_at
        }
