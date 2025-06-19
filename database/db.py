# database/db.py

import aiosqlite

from database.config_db import *

async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                telegram_id INTEGER PRIMARY KEY,
                steam_input TEXT NOT NULL
            )
        """)
        await db.commit()

async def save_user_steam_id(telegram_id: int, steam_input: str):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
            INSERT INTO users (telegram_id, steam_input)
            VALUES (?, ?)
            ON CONFLICT(telegram_id) DO UPDATE SET steam_input = excluded.steam_input
        """, (telegram_id, steam_input))
        await db.commit()

async def get_user_steam_id(telegram_id: int):
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("SELECT steam_input FROM users WHERE telegram_id = ?", (telegram_id,)) as cursor:
            row = await cursor.fetchone()
            return row[0] if row else None