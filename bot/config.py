import os
from dotenv import load_dotenv
from pathlib import Path

# Cargar archivo .env
load_dotenv()

# Variables que el bot necesita
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
PREFIX = os.getenv("PREFIX", "!")
DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{Path('data') / 'bot.db'}")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

