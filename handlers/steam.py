### handlers/steam.py
from aiogram import types, Bot
from aiogram.dispatcher import FSMContext

from handlers.menu import send_main_menu
from states import UserState
from utils.converters import resolve_input_to_steamid64
from database.db import save_user_steam_id
from utils.errors import log_exception

# Эта функция нужна только для inline-кнопки
async def cmd_set_steam_by_id(bot: Bot, telegram_id: int, state: FSMContext):
    await state.set_state(UserState.waiting_for_steam_id)
    await bot.send_message(
        telegram_id,
        "Пожалуйста, введи свой Steam ID или ссылку на профиль (https://steamcommunity.com/id/...)!"
    )

async def cmd_set_steam(message: types.Message, state: FSMContext):
    await state.set_state(UserState.waiting_for_steam_id)
    await message.answer("Пожалуйста, введи свой Steam ID или ссылку на профиль (https://steamcommunity.com/id/...)!")

async def process_steam_id(message: types.Message, state: FSMContext):
    steam_input = message.text.strip()
    try:
        steamid64 = resolve_input_to_steamid64(steam_input)
        await save_user_steam_id(message.from_user.id, steam_input)
        await message.answer("✅ Твой Steam ID успешно сохранён!\nТеперь ты можешь использовать команды для личной статистике.")
        await state.set_state(UserState.idle)
        await send_main_menu(message)
    except Exception as e:
        log_exception(e, context="process_steam_id")
        await message.answer("⚠️ Что-то пошло не так. Проверь Steam ID или ссылку и попробуй снова.")