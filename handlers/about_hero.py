from aiogram import types, Bot
from aiogram.dispatcher import FSMContext

from dota_api.heroes import *
from handlers.menu import send_main_menu
from services.heroes import format_hero_info
from states import UserState
from services.about_hero import build_hero_about_summary
from utils.errors import log_exception

async def cmd_about_hero_by_id(bot: Bot, telegram_id: int, state: FSMContext):
    try:
        await bot.send_message(telegram_id, "Введите имя героя, о котором хотите узнать:")
        await state.set_state(UserState.waiting_for_hero_name)
    except Exception as e:
        log_exception(e, context="cmd_about_hero_by_id")
        await bot.send_message(telegram_id, "⚠️ Ошибка. Попробуйте позже.")

async def cmd_about_hero(message: types.Message, state: FSMContext):
    parts = message.text.strip().split(maxsplit=1)
    if len(parts) > 1:
        hero_name = parts[1]
        summary = build_hero_about_summary(hero_name)
        await message.answer(summary, parse_mode="Markdown")
        await send_main_menu(message)
    else:
        await message.answer("Пожалуйста, введите имя героя:")
        await state.set_state(UserState.waiting_for_about_hero_name)  # ✅ меняем

async def process_about_hero_name(message: types.Message, state: FSMContext):
    text = message.text.strip()

    if text.startswith("/"):
        await state.finish()
        return False

    summary = build_hero_about_summary(text)
    await message.answer(summary, parse_mode="Markdown")
    await state.finish()
    await send_main_menu(message)
    return True

