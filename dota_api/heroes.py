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


def get_hero_stats(hero_id: int) -> dict | None:
    url = "https://api.opendota.com/api/heroStats"
    response = requests.get(url)

    if response.status_code != 200:
        return None

    heroes = response.json()

    for hero in heroes:
        if hero["id"] == hero_id:
            return {
                "roles": hero.get("roles", []),
                "complexity": hero.get("complexity", "—"),
                "winrate": round(hero["win_rate"] * 100, 1) if "win_rate" in hero else round(
                    hero["pro_win"] / hero["pro_pick"] * 100, 1) if hero.get("pro_pick") else None,
                "pick_rate": round(hero["pro_pick"] / sum(h.get("pro_pick", 0) for h in heroes) * 100, 1) if hero.get(
                    "pro_pick") else None,
            }

    return None