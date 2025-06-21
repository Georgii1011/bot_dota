# keyboards/menu.py

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_main_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row(
        KeyboardButton("📊 Общие"),
        KeyboardButton("📅 Матчи")
    )
    kb.row(
        KeyboardButton("🙋 Игроку"),
        KeyboardButton("🦸 Герои")
    )
    kb.row(
        KeyboardButton("🎯 Драфт"),
        KeyboardButton("⚖️ Сравнение")
    )
    kb.row(
        KeyboardButton("🎉 Фан")
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
        KeyboardButton("🚀 Планы на будущее"),
        KeyboardButton("🔙 Назад")
    )

    return kb

def get_matches_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row(
        KeyboardButton("📊 Последняя игра"),
        KeyboardButton("🎮 Последние игры")
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

'''def get_listofheroes_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row(
        KeyboardButton("Ogre Magi"),
        KeyboardButton("Ogre Magi"),
        KeyboardButton("Ogre Magi"),
        KeyboardButton("Ogre Magi"),
        KeyboardButton("Ogre Magi"),
        KeyboardButton("Ogre Magi"),
    )'''

def get_numbers_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row(
        KeyboardButton("1"),
        KeyboardButton("2"),
        KeyboardButton("3"),
        KeyboardButton("4"),
        KeyboardButton("5"),
    )
    kb.row(
        KeyboardButton("6"),
        KeyboardButton("7"),
        KeyboardButton("8"),
        KeyboardButton("9"),
        KeyboardButton("10")
    )

    return kb