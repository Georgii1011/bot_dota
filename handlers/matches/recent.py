# handlers/matches/recent.py

from aiogram import types
from aiogram.dispatcher import FSMContext
from keybords.menu import get_numbers_menu, get_matches_menu
from loader import bot
from services.recent import build_recent_matches_summary
from states import UserState
from database.db import get_user_steam_id
from utils.converters import resolve_input_to_account_id


async def cmd_recent(message: types.Message, state: FSMContext):
    text = message.text.strip()
    parts = text.split(maxsplit=1)

    if text == "🎮 Последние игры":
        await message.answer("Сколько последних матчей показать? Введи число от 1 до 10.", reply_markup=get_numbers_menu())
        await state.set_state(UserState.waiting_for_recent_count)
        return

    current_state = await state.get_state()
    if current_state == UserState.waiting_for_recent_count.state:
        count_str = text
    elif len(parts) == 2:
        count_str = parts[1]
    else:
        await message.answer("Сколько последних матчей показать? Введи число от 1 до 10.")
        await state.set_state(UserState.waiting_for_recent_count)
        return

    if not count_str.isdigit():
        await message.answer("❗ Введи число от 1 до 10.")
        return

    count = int(count_str)
    if count < 1 or count > 10:
        await message.answer("❗ Количество матчей должно быть от 1 до 10.")
        return

    await state.set_state(UserState.idle)

    telegram_id = message.from_user.id
    steam_input = await get_user_steam_id(telegram_id)
    if not steam_input:
        await message.answer("⚠️ Ты ещё не авторизован. Используй /setsteam.")
        return

    account_id = resolve_input_to_account_id(steam_input)
    summary = await build_recent_matches_summary(account_id, count)
    await message.answer(summary, reply_markup=get_matches_menu())
