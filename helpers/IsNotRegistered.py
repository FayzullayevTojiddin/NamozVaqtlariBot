from aiogram.filters import Filter
from aiogram.types import Message
from models.user import User

class IsNotRegistered(Filter):
    async def __call__(self, message: Message, user: User | None) -> bool:
        return user is None