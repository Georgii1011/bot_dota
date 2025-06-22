# handlers/matches/last.py

from utils.converters import *
from services.matches import *
from handlers.utils import *

async def cmd_last(message: types.Message):
    steam_input = await ensure_authorized(message)
    if not steam_input:
        return
    account_id = resolve_input_to_account_id(steam_input)
    summary = build_match_summary(account_id)
    await message.answer(summary)
