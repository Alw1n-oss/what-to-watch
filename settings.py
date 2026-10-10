# what_to_watch/settings.py
import os


class Config(object):
    SECRET_KEY = os.getenv("SECRET_KEY")
    DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
