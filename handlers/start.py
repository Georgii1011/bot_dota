# handlers/start.py
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from handlers.menu import get_main_menu, send_main_menu

async def cmd_start(message: types.Message):
    await message.answer(
        "Привет! Я бот для Dota 2. Если ты ещё не успел авторизоваться, используй /setsteam чтобы авторизоваться и получить доступ к твоей статистике!",
    )
    await send_main_menu(message)