from peewee import *
from .base import database
from .user import User

def create_tables():
    with database:
        database.create_tables([
            User
        ])