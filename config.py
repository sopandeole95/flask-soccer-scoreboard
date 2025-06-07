import os
from dotenv import load_dotenv

load_dotenv()   # reads .env into os.environ

class Config:
    SOCCER_API_TOKEN = os.getenv("SOCCER_API_TOKEN")
    SOCCER_API_URL   = "https://api.football-data.org/v4"  # base URL