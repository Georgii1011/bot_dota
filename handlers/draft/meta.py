# handlers/draft/meta.py

from aiogram import types
from services.meta import *
from utils.errors import *

async def cmd_meta(message: types.Message):
    try:
        summary = build_meta_summary()
        await message.answer(summary)
    except Exception as e:
        log_exception(e, context="cmd_meta")
        await message.answer("⚠️ Что-то пошло не так. Попробуй позже, выбери другую команду или проверь ввод.")