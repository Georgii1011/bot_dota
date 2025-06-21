### handlers/register.py

from aiogram import Dispatcher
from handlers.about_hero import *
from handlers.me import cmd_me
from handlers.start import cmd_start
from handlers.steam import cmd_set_steam, process_steam_id
from handlers.last import cmd_last
from handlers.mystat import cmd_my_stat
from handlers.meta import cmd_meta
from handlers.contr import cmd_contr, process_hero_name
from handlers.fallback import unknown_message
from handlers.help import cmd_help
from handlers.recent import *


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=["start"], state="*")
    dp.register_message_handler(cmd_me, commands=["me"], state="*")
    dp.register_message_handler(cmd_last, commands=["last"], state="*")
    dp.register_message_handler(cmd_contr, commands=["contr"], state="*")
    dp.register_message_handler(process_hero_name, state=UserState.waiting_for_hero_name)
    dp.register_message_handler(cmd_meta, commands=["meta"], state="*")
    dp.register_message_handler(cmd_my_stat, commands=["mystat"], state="*")
    dp.register_message_handler(cmd_set_steam, commands=["setsteam"], state="*")
    dp.register_message_handler(process_steam_id, state=UserState.waiting_for_steam_id)
    dp.register_message_handler(cmd_help, commands=["help"], state="*")
    dp.register_message_handler(cmd_recent, commands=["recent"], state="*")
    dp.register_message_handler(cmd_about_hero, commands=["about_hero"], state="*")
    dp.register_message_handler(process_about_hero_name, state=UserState.waiting_for_about_hero_name)
    dp.register_message_handler(cmd_recent, state=UserState.waiting_for_recent_count)

    dp.register_message_handler(cmd_last, lambda msg: msg.text == "📊 Последняя игра", state="*")
    dp.register_message_handler(cmd_contr, lambda msg: msg.text == "🛡 Контрпики", state="*")
    dp.register_message_handler(process_hero_name, state=UserState.waiting_for_hero_name)
    dp.register_message_handler(cmd_meta, lambda msg: msg.text == "🔥 Лучшие герои", state="*")
    dp.register_message_handler(cmd_my_stat, lambda msg: msg.text == "📈 Моя статистика", state="*")
    dp.register_message_handler(cmd_set_steam, lambda msg: msg.text == "🧾 Установить Steam ID", state="*")
    dp.register_message_handler(cmd_help, lambda msg: msg.text == "ℹ️ Помощь", state="*")

    dp.register_message_handler(unknown_message, content_types=types.ContentTypes.TEXT, state="*")
