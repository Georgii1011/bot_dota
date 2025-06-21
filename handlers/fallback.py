### handlers/fallback.py

from aiogram import types
from aiogram.dispatcher import FSMContext
from states import UserState

async def unknown_message(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state != UserState.waiting_for_steam_id.state:
        await message.reply("Пожалуйста, выбери одну из команд из меню или напиши /start, чтобы начать заново.")
