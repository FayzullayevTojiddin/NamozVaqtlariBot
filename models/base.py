from peewee import *
from config import Config
import datetime

database = MySQLDatabase(
    Config.database['name'],
    password=Config.database['password'],
    user=Config.database['user'],
    host=Config.database['host'],
    port=Config.database['port']
)

class BaseModel(Model):
    id = AutoField()
    created_at = DateTimeField(default=datetime.datetime.now)
    class Meta:
        database = database