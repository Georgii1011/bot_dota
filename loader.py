# loader.py

from aiogram.contrib.fsm_storage.memory import *
from aiogram import *
from config import *

storage = MemoryStorage()
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)