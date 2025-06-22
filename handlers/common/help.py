# handler/common/help.py

from aiogram import types

async def cmd_help(message: types.Message):
    help_text = (
        "🛠 Доступные команды:\n\n"
        "/start — Запустить бота и показать меню\n"
        "/help — Показать это сообщение\n"
        "/setsteam — Установить или обновить Steam ID\n"
        "/me — Узнать информацию о себе\n"
        "/last — Показать последнию игру\n"
        "/recent — Показать несколько последних игр"
        "/contr <герой> — Показать контрпики против героя\n"
        "/meta — Показать текущую мету героев\n"
        "/mystat — Показать твою статистику (требуется авторизация)\n"
    )
    await message.answer(help_text)