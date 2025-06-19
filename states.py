# states.py
# для aiogram 2.x
from aiogram.dispatcher.filters.state import State, StatesGroup

class UserState(StatesGroup):
    idle = State()
    waiting_for_command_input = State()
    waiting_for_steam_id = State()
    waiting_for_hero_name = State()
    waiting_for_recent_count = State()