import asyncio
from aiogram import Bot, Dispatcher
from config import Config
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode
from handlers import router
from models import create_tables
from middlewares.auth import AuthMiddleware

bot = Bot(token=Config.bot_token, default=DefaultBotProperties(
    parse_mode=ParseMode.MARKDOWN
))

dp = Dispatcher()
dp.include_router(router)
dp.update.middleware(AuthMiddleware())

async def main():
    create_tables()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())