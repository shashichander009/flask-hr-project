import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = "postgresql://shashi:shashi@localhost:5432/mbhr"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
