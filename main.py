# import os
# import uuid
#
# from flask import Flask, jsonify, request
# from sqlalchemy import create_engine, Column, String, DateTime, func, Text, ForeignKey
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker, relationship
#
# database_location = os.path.join(
#     os.getcwd(), 'db.sqlite3'
# )
#
# engine = create_engine(
#     f'sqlite:///{database_location}',
#     echo=True,
#     connect_args={'check_same_thread': False}
# )
#
# Base = declarative_base()
# Session = sessionmaker(bind=engine)
# session = Session()
#
#
# class User(Base):
#     __tablename__ = 'users'
#
#     id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
#     username = Column(String(20), nullable=False)
#     created_at = Column(
#         DateTime(timezone=True),
#         server_default=func.now()
#     )
#
#     posts = relationship('Post', back_populates='user')
#
#     def serialize(self):
#         return {
#             'id': self.id,
#             'username': self.username,
#             'created_at': self.created_at,
#             'posts': [post.serialize() for post in self.posts]
#         }
#
#     def __repr__(self):
#         return f"<User(id='{self.id}', username='{self.username}')>"
#
#
# class Post(Base):
#     __tablename__ = 'posts'
#
#     id = Column(
#         String(36),
#         primary_key=True,
#         default=lambda: str(uuid.uuid4())
#     )
#     id_user = Column(String(36), ForeignKey('users.id'))
#     title = Column(String(50), nullable=False)
#     text = Column(Text, nullable=False)
#     created_at = Column(
#         DateTime(timezone=True),
#         server_default=func.now()
#     )
#     updated_at = Column(
#         DateTime(timezone=True),
#         onupdate=func.now()
#     )
#
#     user = relationship('User', back_populates='posts', uselist=False)
#
#     def serialize(self):
#         return {
#             'id': self.id,
#             'username': self.user.username,
#             'title': self.title,
#             'text': self.text,
#             'created_at': self.created_at,
#             'updated_at': self.updated_at
#         }
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def index():
#     return jsonify('Hello')
#
#
# @app.route('/users', methods=['GET'])
# def get_all_users():
#     return jsonify([
#         user.serialize() for user in session.query(User).all()
#     ])
#
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     data = request.get_json()
#     username = data.get('username', 'anonymous')
#
#     user = User(username=username)
#     session.add(user)
#     session.commit()
#
#     return jsonify(user.serialize()), 201
#
#
# @app.route('/posts', methods=['GET'])
# def get_all_posts():
#     return jsonify([
#         post.serialize() for post in session.query(Post).all()
#     ])
#
#
# @app.route('/posts', methods=['POST'])
# def create_post():
#     data = request.get_json()
#     id_user = data.get('id_user')
#     title = data.get('title')
#     text = data.get('text')
#
#     post = Post(id_user=id_user, title=title, text=text)
#     session.add(post)
#     session.commit()
#
#     return jsonify(post.serialize()), 201
#
#
# Base.metadata.create_all(engine)
#
# if session.query(User).count() == 0:
#     user = User(username='pythondev')
#     session.add(user)
#     session.commit()
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
