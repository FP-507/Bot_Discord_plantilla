import aiosqlite
import asyncio
from pathlib import Path

DB_PATH = Path("data")
DB_PATH.mkdir(parents=True, exist_ok=True)
DB_FILE = DB_PATH / "bot.db"

async def init_db():
    async with aiosqlite.connect(str(DB_FILE)) as db:
        await db.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                discord_id INTEGER UNIQUE,
                username TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        await db.commit()

async def add_or_update_user(discord_id: int, username: str):
    async with aiosqlite.connect(str(DB_FILE)) as db:
        await db.execute(
            """
            INSERT INTO users (discord_id, username)
            VALUES (?, ?)
            ON CONFLICT(discord_id) DO UPDATE SET
                username = excluded.username
            """,
            (discord_id, username),
        )
        await db.commit()

async def get_user_count() -> int:
    async with aiosqlite.connect(str(DB_FILE)) as db:
        cur = await db.execute("SELECT COUNT(*) FROM users")
        row = await cur.fetchone()
        return row[0] if row else 0

def ensure_db(loop: asyncio.AbstractEventLoop):
    """Helper para inicializar la DB desde contexto síncrono"""
    loop.run_until_complete(init_db())
