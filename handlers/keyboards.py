# handlers/keyboards.py

from aiogram import types
from keybords.menu import *

# Главное меню
async def show_main_menu(message: types.Message):
    #await message.delete()
    await message.answer("Выбери раздел:", reply_markup=get_main_menu())

# Подменю
async def show_common_menu(message: types.Message):
    #await message.delete()
    await message.answer("Общие команды:", reply_markup=get_common_menu())

async def show_matches_menu(message: types.Message):
    #await message.delete()
    await message.answer("Информация о матчах:", reply_markup=get_matches_menu())

async def show_player_menu(message: types.Message):
    #await message.delete()
    await message.answer("Игровая статистика:", reply_markup=get_player_menu())

async def show_heroes_menu(message: types.Message):
    #await message.delete()
    await message.answer("Аналитика по героям:", reply_markup=get_heroes_menu())

async def show_meta_menu(message: types.Message):
    #await message.delete()
    await message.answer("Мета герои:", reply_markup=get_meta_menu())

async def show_comprasion_menu(message: types.Message):
    #await message.delete()
    await message.answer("Сравнение игроков или героев:", reply_markup=get_comprasion_menu())

async def show_fun_menu(message: types.Message):
    #await message.delete()
    await message.answer("Развлечения:", reply_markup=get_fun_menu())
