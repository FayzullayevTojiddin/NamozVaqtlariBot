from aiogram import BaseMiddleware
from aiogram.types import Update
from typing import Callable, Dict, Any, Awaitable
from models.user import User

class AuthMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
        event: Update,
        data: Dict[str, Any],
    ) -> Any:
        if event.message:
            user_from = event.message.from_user

        elif event.callback_query:
            user_from = event.callback_query.from_user

        user = User.get_or_none(User.id == user_from.id)
        if not user:
            User.create(
                id=user_from.id,
            )
            data["user"] = None
        else:
            data["user"] = user
            
        return await handler(event, data)