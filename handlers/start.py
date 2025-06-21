# handlers/start.py

from aiogram import types
from handlers.menu import *

async def cmd_start(message: types.Message):
    await message.answer(
        "Привет! Я бот для Dota 2. Если ты ещё не успел авторизоваться, "
        "используй /setsteam чтобы авторизоваться и получить доступ к твоей статистике!",
    reply_markup = get_main_reply_keyboard()
    )