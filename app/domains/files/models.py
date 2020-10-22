import uuid

from sqlalchemy import func

from database import db


class File(db.Model):
    __tablename__ = 'files'

    id = db.Column(
        db.String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()))

    name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(
        db.DateTime(timezone=True),
        server_default=func.now()
    )

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'created_at': self.created_at
        }