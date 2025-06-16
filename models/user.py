from datetime import datetime
from peewee import BigIntegerField, CharField, DateTimeField
from .base import BaseModel

class User(BaseModel):
    id = BigIntegerField(primary_key=True)
    region = CharField(null=True)
    created_at = DateTimeField(default=datetime.now)

    class Meta:
        table_name = 'users'

    @classmethod
    def change_region(cls, user_id, region):
        user = cls.get_or_none(cls.id == user_id)
        if user:
            user.region = region
            user.save()
            return user
        return None