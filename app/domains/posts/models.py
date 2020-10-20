import uuid

from sqlalchemy import func

from database import db


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(
        db.String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )
    user_id = db.Column(
        db.String(36), db.ForeignKey('users.id')
    )
    title = db.Column(db.String(50), nullable=False)
    text = db.Column(db.Text(), nullable=False)
    created_at = db.Column(
        db.DateTime(timezone=True), server_default=func.now()
    )
    updated_at = db.Column(
        db.DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    user = db.relationship(
        'User', back_populates='posts', uselist=False
    )

    def serialize(self):
        author = "{} {}".format(
            self.user.profile.first_name,
            self.user.profile.last_name
        )

        return {
            'id': self.id,
            'author': author,
            'title': self.title,
            'text': self.text
        }
