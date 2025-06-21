# setcommads.py

# команды меню
from aiogram import Bot
from aiogram.types import BotCommand

async def set_bot_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Приветствие и инструкция, обновление бота"),
        BotCommand(command="/help", description="Список всех команд"),
        BotCommand(command="/setsteam", description="Ввести новый стим"),
        BotCommand(command="/me", description="Информация о регистрации"),
        BotCommand(command="/future", description="Планы на будущее"),
        BotCommand(command="/contr", description="Контрпики против героя"),
        BotCommand(command="/last", description="Последняя игра Dota 2"),
        BotCommand(command="/meta", description="Лучшие герои патча"),
        BotCommand(command="/mystat", description="Ваша личная статистика"),
        BotCommand(command="/recent", description="Последние ваши игры"),
        BotCommand(command="/about_hero", description="Информация о герое")
    ]
    await bot.set_my_commands(commands)