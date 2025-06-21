from aiogram import types
from aiogram.dispatcher import FSMContext

from states import UserState
from services.about_hero import build_hero_about_summary

async def cmd_about_hero(message: types.Message, state: FSMContext):
    parts = message.text.strip().split(maxsplit=1)
    if len(parts) > 1:
        hero_name = parts[1]
        summary = build_hero_about_summary(hero_name)
        await message.answer(summary, parse_mode="Markdown")
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
    return True

