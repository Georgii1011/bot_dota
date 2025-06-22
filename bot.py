# bot.py

from database.db import *
from handlers.register import *
from setcommands import *
from loader import *

async def on_startup(dp):
    await init_db()
    await set_bot_commands(dp.bot)
    print("База данных инициализирована.")

if __name__ == "__main__":
    print("Бот запущен")
    register_handlers(dp)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)