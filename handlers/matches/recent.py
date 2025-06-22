# handlers/matches/recent.py

from aiogram import types
from aiogram.dispatcher import FSMContext
from keybords.menu import *
from services.recent import *
from states import *
from database.db import *
from utils.converters import *

async def cmd_recent(message: types.Message, state: FSMContext):
    await message.answer(
        "Сколько последних матчей показать? Введи число от 1 до 10.",
        reply_markup=get_numbers_menu()
    )
    await state.set_state(UserState.waiting_for_recent_count)

async def process_recent_count(message: types.Message, state: FSMContext):
    text = message.text.strip()

    if not text.isdigit():
        await message.answer("❗ Введи число от 1 до 10.")
        return  # НЕ сбрасываем состояние — пользователь может ввести снова

    count = int(text)
    if not (1 <= count <= 10):
        await message.answer("❗ Количество матчей должно быть от 1 до 10.")
        return

    telegram_id = message.from_user.id
    steam_input = await get_user_steam_id(telegram_id)
    if not steam_input:
        await message.answer("⚠️ Ты ещё не авторизован. Используй /setsteam.")
        await state.finish()
        return

    account_id = resolve_input_to_account_id(steam_input)
    summary = await build_recent_matches_summary(account_id, count)

    await message.answer(summary, reply_markup=get_matches_menu())
    await state.finish()
