# handlers/menu.py

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_main_reply_keyboard():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row(
        KeyboardButton("📊 Последняя игра"),
        KeyboardButton("🛡 Контрпики")
    )
    kb.row(
        KeyboardButton("🔥 Лучшие герои"),
        KeyboardButton("📈 Моя статистика")
    )
    kb.row(
        KeyboardButton("🧾 Установить Steam ID"),
        KeyboardButton("ℹ️ Помощь")
    )
    return kb
