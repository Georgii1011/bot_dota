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
            total_pro_picks = sum(h.get("pro_pick", 0) for h in heroes)
            return {
                "roles": hero.get("roles", []),
                "primary_attr": hero.get("primary_attr"),
                "attack_type": hero.get("attack_type"),
                "base_attack_min": hero.get("base_attack_min"),
                "base_attack_max": hero.get("base_attack_max"),
                "attack_rate": hero.get("attack_rate"),
                "base_armor": hero.get("base_armor"),
                "attack_range": hero.get("attack_range"),
                "move_speed": hero.get("move_speed"),
                "base_health": hero.get("base_health"),
                "base_health_regen": hero.get("base_health_regen"),
                "base_mana": hero.get("base_mana"),
                "base_mana_regen": hero.get("base_mana_regen"),
                "base_str": hero.get("base_str"),
                "base_agi": hero.get("base_agi"),
                "base_int": hero.get("base_int"),
                "str_gain": hero.get("str_gain"),
                "agi_gain": hero.get("agi_gain"),
                "int_gain": hero.get("int_gain"),
                "winrate": round(hero["win_rate"] * 100, 1) if "win_rate" in hero else round(
                    hero["pro_win"] / hero["pro_pick"] * 100, 1) if hero.get("pro_pick") else None,
                "pick_rate": round(hero["pro_pick"] / total_pro_picks * 100, 1) if hero.get("pro_pick") else None,
            }

    return None
