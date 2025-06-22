# handlers/common/steam.py

from aiogram import types
from aiogram.dispatcher import FSMContext
from states import UserState
#from utils.converters import *
from database.db import *
from utils.errors import *

async def cmd_set_steam(message: types.Message, state: FSMContext):
    await state.set_state(UserState.waiting_for_steam_id)
    await message.answer("Пожалуйста, введи свой Steam ID или ссылку на профиль (https://steamcommunity.com/id/...)!")

async def process_steam_id(message: types.Message, state: FSMContext):
    steam_input = message.text.strip()
    try:
        #steamid64 = resolve_input_to_steamid64(steam_input)
        await save_user_steam_id(message.from_user.id, steam_input)
        await message.answer("✅ Твой Steam ID успешно сохранён!\nТеперь ты можешь использовать команды для личной статистике.")
        await state.set_state(UserState.idle)
    except Exception as e:
        log_exception(e, context="process_steam_id")
        await message.answer("⚠️ Что-то пошло не так. Проверь Steam ID или ссылку и попробуй снова.")