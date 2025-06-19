# handler/help.py

from aiogram import types

from handlers.menu import send_main_menu


async def cmd_help(message: types.Message):
    help_text = (
        "🛠 Доступные команды:\n\n"
        "/start — Запустить бота и показать меню\n"
        "/contr <герой> — Показать контрпики против героя\n"
        "/last — Показать последнию игру\n"
        "/meta — Показать текущую мету героев\n"
        "/mystat — Показать твою статистику (требуется авторизация)\n"
        "/setsteam — Установить или обновить Steam ID\n"
        "/help — Показать это сообщение\n"
    )
    await message.answer(help_text)
    await send_main_menu(message)