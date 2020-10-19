import os

from dotenv import load_dotenv

load_dotenv()

database_file = os.path.join(os.getcwd(), 'db.sqlite3')

FLASK_APP = 'run'
DEBUG = os.getenv('DEBUG', True)
SECRET_KEY = os.getenv('SECRET_KEY')
SQLALCHEMY_DATABASE_URI = f'sqlite:///{database_file}'
SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS', True)
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')
