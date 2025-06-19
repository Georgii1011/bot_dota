### handlers/meta.py
from aiogram import types

from handlers.menu import send_main_menu
from services.meta import build_meta_summary
from utils.errors import log_exception

async def cmd_meta(message: types.Message):
    try:
        summary = build_meta_summary()
        await message.answer(summary)
        await send_main_menu(message)
    except Exception as e:
        log_exception(e, context="cmd_meta")
        await message.answer("⚠️ Что-то пошло не так. Попробуй позже, выбери другую команду или проверь ввод.")
        await send_main_menu(message)