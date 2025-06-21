# handlers/heroes/contr.py

from aiogram import types
from aiogram.dispatcher import FSMContext

from states import UserState
from services.contr import build_counters_summary
from utils.errors import log_exception

async def cmd_contr(message: types.Message, state: FSMContext):
    try:
        text = message.text.strip()

        # Обработка вызова с кнопки (например, "🛡 Контрпики")
        if text == "🛡 Контрпики" or text == "/contr":
            await message.answer("Пожалуйста, введи имя героя:")
            await state.set_state(UserState.waiting_for_hero_name)
            return

        # Обработка ввода в виде: /contr axe
        parts = text.split(maxsplit=1)
        if len(parts) > 1 and parts[0] == "/contr":
            hero_name = parts[1]
            summary = build_counters_summary(hero_name)
            await message.answer(summary)
        else:
            # если просто написали имя героя без /contr
            summary = build_counters_summary(text)
            await message.answer(summary)

    except Exception as e:
        log_exception(e, context="cmd_contr")
        await message.answer("⚠️ Что-то пошло не так. Попробуй позже или проверь ввод.")

async def process_hero_name(message: types.Message, state: FSMContext):
    text = message.text.strip()

    if text.startswith("/"):
        await state.finish()
        return False

    summary = build_counters_summary(text)
    if summary.startswith("Герой не найден"):
        await message.answer(summary + "\nПопробуй ещё раз или введи /contr для выхода.")
        return True

    await message.answer(summary)
    await state.finish()
    return True


