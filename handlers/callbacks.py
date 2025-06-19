from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.utils.exceptions import MessageNotModified

# Импортируй нужные команды
from handlers.last import cmd_last, cmd_last_by_id
from handlers.contr import cmd_contr, cmd_contr_by_id
from handlers.menu import send_main_menu
from handlers.meta import cmd_meta
from handlers.mystat import cmd_my_stat, cmd_my_stat_by_id
from handlers.steam import cmd_set_steam, cmd_set_steam_by_id
from handlers.help import cmd_help

def register_callback_handlers(dp: Dispatcher):
    @dp.callback_query_handler(lambda c: c.data in ["last", "contr", "meta", "mystat", "setsteam", "help"], state="*")
    async def process_callback(callback_query: types.CallbackQuery):
        message = callback_query.message
        data = callback_query.data
        telegram_id = callback_query.from_user.id

        try:
            if data == "last":
                # await message.answer("Показываю последний матч...")
                result = await cmd_last_by_id(telegram_id)
                summary, keyboard = result
                await message.answer(summary, reply_markup=keyboard)
            elif data == "contr":
                await cmd_contr_by_id(callback_query.bot, telegram_id, state=dp.current_state(user=telegram_id))
            elif data == "meta":
                # await message.answer("Показываю мету...")
                await cmd_meta(message)
            elif data == "mystat":
                msg = await cmd_my_stat_by_id(telegram_id)
                await message.answer(msg, parse_mode="Markdown")
                await send_main_menu(message)
            elif data == "setsteam":
                await cmd_set_steam_by_id(callback_query.bot, telegram_id, state=dp.current_state(user=telegram_id))
            elif data == "help":
                # await message.answer("Одну секудну...")
                await cmd_help(message)

        finally:
            try:
            # Убираем inline-клавиатуру, чтобы кнопка снова работала
                await callback_query.message.edit_text(
                    callback_query.message.text,
                    reply_markup=callback_query.message.reply_markup
                )
            except MessageNotModified:
                pass
            #await callback_query.message.edit_reply_markup(reply_markup=None)
            await callback_query.answer()
