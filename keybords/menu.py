# keyboards/menu.py

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_main_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row(
        KeyboardButton("Общие"),
        KeyboardButton("Матчи")
    )
    kb.row(
        KeyboardButton("Игроку"),
        KeyboardButton("Герои")
    )
    kb.row(
        KeyboardButton("Драфт"),
        KeyboardButton("Сравнение")
    )
    kb.row(
        KeyboardButton("Фан")
    )

    return kb

def get_common_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row(
        KeyboardButton("👋🤖 Привествие или обновление бота"),
        KeyboardButton("ℹ️ Помощь")
    )
    kb.row(
        KeyboardButton("🧾 Установить Steam ID"),
        KeyboardButton("ℹ️ Информация обо мне")
    )
    kb.row(
        KeyboardButton("🔙 Назад")
    )

    return kb

def get_matches_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row(
        KeyboardButton("📊 Последняя игра")
    )
    kb.row(
        KeyboardButton("🔙 Назад")
    )

    return kb

def get_player_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row(
        KeyboardButton("📈 Моя статистика")
    )
    kb.row(
        KeyboardButton("🔙 Назад")
    )

    return kb

def get_heroes_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row(
        KeyboardButton("🛡 Контрпики")
    )
    kb.row(
        KeyboardButton("🔙 Назад")
    )

    return kb

def get_meta_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row(
        KeyboardButton("🔥 Лучшие герои")
    )
    kb.row(
        KeyboardButton("🔙 Назад")
    )

    return kb

def get_comprasion_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row(
        KeyboardButton("🔙 Назад")
    )

    return kb

def get_fun_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row(
        KeyboardButton("🔙 Назад")
    )

    return kb
