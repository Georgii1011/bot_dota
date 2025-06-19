from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# Функция, возвращающая InlineKeyboardMarkup
def get_main_menu():
    inline_kb = InlineKeyboardMarkup(row_width=2)
    inline_kb.add(
        InlineKeyboardButton("📊 Последняя игра", callback_data="last"),
        InlineKeyboardButton("🛡 Контрпики", callback_data="contr"),
        InlineKeyboardButton("🔥 Лучшие герои", callback_data="meta"),
        InlineKeyboardButton("📈 Моя статистика", callback_data="mystat"),
        InlineKeyboardButton("🧾 Установить Steam ID", callback_data="setsteam"),
        InlineKeyboardButton("ℹ️ Помощь", callback_data="help"),
        # InlineKeyboardButton("Последние матчи!", callback_data="recent")
    )
    return inline_kb

async def send_main_menu(message: types.Message):
    await message.answer("Выбери действие: ", reply_markup=get_main_menu())
