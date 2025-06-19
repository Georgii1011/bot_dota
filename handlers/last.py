### handlers/last.py
from aiogram import *

from handlers.menu import get_main_menu, send_main_menu
from utils.converters import resolve_input_to_account_id
from services.matches import build_match_summary
from handlers.utils import ensure_authorized
from handlers.utils import get_user_steam_id

async def cmd_last(message: types.Message):
    steam_input = await ensure_authorized(message)
    if not steam_input:
        return
    account_id = resolve_input_to_account_id(steam_input)
    summary = build_match_summary(account_id)
    await message.answer(summary)
    await send_main_menu(message)


async def cmd_last_by_id(telegram_id: int):
    steam_input = await get_user_steam_id(telegram_id)
    if not steam_input:
        return "⚠️ Ты ещё не авторизован. Используй /setsteam"

    try:
        account_id = resolve_input_to_account_id(steam_input)
    except ValueError as e:
        return f"⚠️ Ошибка: {e}"
    except Exception:
        return "⚠️ Не удалось определить Steam ID. Попробуй позже."

    summary = build_match_summary(account_id)
    return summary, get_main_menu()
