# handlers/utils.py

from database.db import get_user_steam_id
from aiogram import *


async def ensure_authorized(message: types.Message) -> str | None:
    steam_input = await get_user_steam_id(message.from_user.id)
    if not steam_input:
        await message.answer("⚠️ Ты ещё не авторизован. Используй /setsteam, чтобы авторизоваться.")
        return None
    return steam_input