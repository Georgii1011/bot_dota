### handlers/last.py
from aiogram import *
from utils.converters import resolve_input_to_account_id
from services.matches import build_match_summary
from handlers.utils import ensure_authorized

async def cmd_last(message: types.Message):
    steam_input = await ensure_authorized(message)
    if not steam_input:
        return
    account_id = resolve_input_to_account_id(steam_input)
    summary = build_match_summary(account_id)
    await message.answer(summary)
