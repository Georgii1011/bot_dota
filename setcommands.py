# setcommads.py
# команды меню
from aiogram import Bot
from aiogram.types import BotCommand

async def set_bot_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Приветствие и инструкция"),
        BotCommand(command="/contr", description="Контрпики против героя"),
        BotCommand(command="/last", description="Последняя игра Dota 2"),
        BotCommand(command="/meta", description="Лучшие герои патча"),
        BotCommand(command="/mystat", description="Ваша личная статистика"),
        BotCommand(command="/setsteam", description="Ввести новый стим"),
        BotCommand(command="/help", description="Список всех команд"),
        # BotCommand(command="/recent", description="Последние ваши игры")
    ]
    await bot.set_my_commands(commands)