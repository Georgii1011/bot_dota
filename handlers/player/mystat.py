# handlers/player/mystat.py

from utils.converters import *
from services.player import *
from handlers.utils import *
from utils.errors import *

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

