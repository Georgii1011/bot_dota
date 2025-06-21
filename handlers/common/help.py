# handler/common/help.py

from aiogram import types

async def cmd_help(message: types.Message):
    help_text = (
        "🛠 Доступные команды:\n\n"
        "/start — Запустить бота и показать меню\n"
        "/contr <герой> — Показать контрпики против героя\n"
        "/last — Показать последнию игру\n"
        "/druft — Показать текущую мету героев\n"
        "/mystat — Показать твою статистику (требуется авторизация)\n"
        "/setsteam — Установить или обновить Steam ID\n"
        "/help — Показать это сообщение\n"
    )
    await message.answer(help_text)