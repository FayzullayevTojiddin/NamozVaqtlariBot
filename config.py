from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    bot_token = os.getenv("BOT_TOKEN")
    database = {
        "name": os.getenv("DB_NAME"),
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD"),
        "host": os.getenv("DB_HOST"),
        "port": int(os.getenv("DB_PORT")),
    }
