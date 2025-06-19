### handlers/contr.py
from aiogram import types, Bot
from aiogram.dispatcher import FSMContext

from handlers.menu import send_main_menu
from states import UserState
from services.contr import build_counters_summary
from utils.errors import log_exception

async def cmd_contr_by_id(bot: Bot, telegram_id: int, state: FSMContext):
    try:
        await bot.send_message(telegram_id, "Пожалуйста, введи имя героя:")
        await state.set_state(UserState.waiting_for_hero_name)
    except Exception as e:
        log_exception(e, context="cmd_contr_by_id")
        await bot.send_message(telegram_id, "⚠️ Что-то пошло не так. Попробуй позже или проверь ввод.")

async def cmd_contr(message: types.Message, state: FSMContext):
    try:
        parts = message.text.strip().split(maxsplit=1)
        if len(parts) > 1:
            hero_name = parts[1]
            summary = build_counters_summary(hero_name)
            await message.answer(summary)
            await send_main_menu(message)
        else:
            await message.answer("Пожалуйста, введи имя героя:")
            await state.set_state(UserState.waiting_for_hero_name)
    except Exception as e:
        log_exception(e, context="cmd_contr")
        await message.answer("⚠️ Что-то пошло не так. Попробуй позже или проверь ввод.")

async def process_hero_name(message: types.Message, state: FSMContext):
    text = message.text.strip()

    if text.startswith("/"):
        # Сбрасываем состояние ожидания героя
        await state.finish()
        # Возвращаем False, чтобы aiogram передал сообщение дальше
        return False

    summary = build_counters_summary(text)
    if summary.startswith("Герой не найден"):
        await message.answer(summary + "\nПопробуй ещё раз или введи /contr для выхода.")
        return True  # сообщение обработано, ждём новый ввод

    await message.answer(summary)
    await state.finish()
    await send_main_menu(message)
    return True


