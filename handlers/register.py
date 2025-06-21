# handlers/register.py

from aiogram import Dispatcher

from handlers.common.future import cmd_future
from handlers.heroes.about_hero import *
from handlers.common.me import cmd_me
from handlers.common.start import cmd_start
from handlers.common.steam import cmd_set_steam, process_steam_id
from handlers.matches.last import cmd_last
from handlers.player.mystat import cmd_my_stat
from handlers.draft.meta import cmd_meta
from handlers.heroes.contr import cmd_contr, process_hero_name
from handlers.fallback import unknown_message
from handlers.common.help import cmd_help
from handlers.matches.recent import *
from handlers.keyboards import *


def register_handlers(dp: Dispatcher):
    # Обработка консольных команд
    dp.register_message_handler(cmd_start, commands=["start"], state="*")
    dp.register_message_handler(cmd_help, commands=["help"], state="*")
    dp.register_message_handler(cmd_set_steam, commands=["setsteam"], state="*")
    dp.register_message_handler(cmd_me, commands=["me"], state="*")
    dp.register_message_handler(cmd_future, commands=["future"], state="*")
    dp.register_message_handler(cmd_last, commands=["last"], state="*")
    dp.register_message_handler(cmd_contr, commands=["contr"], state="*")
    dp.register_message_handler(cmd_meta, commands=["meta"], state="*")
    dp.register_message_handler(cmd_my_stat, commands=["mystat"], state="*")
    dp.register_message_handler(cmd_recent, commands=["recent"], state="*")
    dp.register_message_handler(cmd_about_hero, commands=["about_hero"], state="*")

    # Обработка команд из меню
    # Общее меню
    dp.register_message_handler(cmd_start, lambda msg: msg.text == "👋🤖 Привествие или обновление бота", state="*")
    dp.register_message_handler(cmd_help, lambda msg: msg.text == "ℹ️ Помощь", state="*")
    dp.register_message_handler(cmd_set_steam, lambda msg: msg.text == "🧾 Установить Steam ID", state="*")
    dp.register_message_handler(cmd_me, lambda msg: msg.text == "ℹ️ Информация обо мне", state="*")
    dp.register_message_handler(cmd_future, lambda msg: msg.text == "🚀 Планы на будущее", state="*")

    # Меню матчей
    dp.register_message_handler(cmd_last, lambda msg: msg.text == "📊 Последняя игра", state="*")
    dp.register_message_handler(cmd_recent, lambda msg: msg.text == "🎮 Последние игры", state="*")

    # Меню игрока
    dp.register_message_handler(cmd_my_stat, lambda msg: msg.text == "📈 Моя статистика", state="*")

    # Меню героев
    dp.register_message_handler(cmd_contr, lambda msg: msg.text == "🛡 Контрпики", state="*")

    # Меню драфта
    dp.register_message_handler(cmd_meta, lambda msg: msg.text == "🔥 Лучшие герои", state="*")

    # Обработка команды назад
    dp.register_message_handler(show_main_menu, lambda msg: msg.text == "🔙 Назад", state="*")

    # Переход в подменю
    dp.register_message_handler(show_common_menu, lambda msg: msg.text == "📊 Общие", state="*")
    dp.register_message_handler(show_matches_menu, lambda msg: msg.text == "📅 Матчи", state="*")
    dp.register_message_handler(show_player_menu, lambda msg: msg.text == "🙋 Игроку", state="*")
    dp.register_message_handler(show_heroes_menu, lambda msg: msg.text == "🦸 Герои", state="*")
    dp.register_message_handler(show_meta_menu, lambda msg: msg.text == "🎯 Драфт", state="*")
    dp.register_message_handler(show_comprasion_menu, lambda msg: msg.text == "⚖️ Сравнение", state="*")
    dp.register_message_handler(show_fun_menu, lambda msg: msg.text == "🎉 Фан", state="*")

    #Обработка состояний
    dp.register_message_handler(process_hero_name, state=UserState.waiting_for_hero_name)
    dp.register_message_handler(process_steam_id, state=UserState.waiting_for_steam_id)
    dp.register_message_handler(process_about_hero_name, state=UserState.waiting_for_about_hero_name)
    dp.register_message_handler(cmd_recent, state=UserState.waiting_for_recent_count)

    #Обработка неизвестной команды (всегда должна быть в конце)
    dp.register_message_handler(unknown_message, content_types=types.ContentTypes.TEXT, state="*")
