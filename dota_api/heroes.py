# dota_api/heroes.py

import requests
from utils.name_heroes import *

def get_hero_dict():
    response = requests.get("https://api.opendota.com/api/heroes")
    data = response.json()
    return {hero["id"]: hero["localized_name"] for hero in data}

def get_hero_matchups(hero_id: int) -> list:
    url = f"https://api.opendota.com/api/heroes/{hero_id}/matchups"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

hero_dict = get_hero_dict()
name_to_id = {v: k for k, v in hero_dict.items()}

def resolve_hero_name(user_input: str) -> str | None:
    user_input = user_input.strip().lower()

    if user_input in aliases:
        return aliases[user_input]

    return None