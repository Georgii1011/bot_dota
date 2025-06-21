# handlers/player/mystat.py

from aiogram import types
from utils.converters import resolve_input_to_account_id
from services.player import format_player_stats_message
from handlers.utils import ensure_authorized
from utils.errors import log_exception

async def cmd_my_stat(message: types.Message):
    steam_input = await ensure_authorized(message)
    if not steam_input:
        return
    try:
        account_id = resolve_input_to_account_id(steam_input)
        msg = format_player_stats_message(steam_input, account_id)
        await message.answer(msg, parse_mode="Markdown")
    except Exception as e:
        log_exception(e, context="cmd_my_stat")
        await message.answer("⚠️ Что-то пошло не так. Попробуй позже или проверь ввод.")

