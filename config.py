import os
from dotenv import load_dotenv

load_dotenv()  # reads .env into os.environ


class Config:
    SOCCER_API_TOKEN = os.getenv("SOCCER_API_TOKEN")
    SOCCER_API_URL = "https://api.football-data.org/v4"  # base URL

    # DATABASE_URL from .env, fallback to SQLite for local dev
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///soccer.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
