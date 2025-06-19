# utils/converters.py

import re
import requests
from utils.config_utils import *

def resolve_input_to_account_id(user_input: str) -> int:
    steamid_64 = resolve_input_to_steamid64(user_input)
    return steamid_64 - int(STEAM_BASE)

def resolve_input_to_steamid64(user_input: str) -> int:
    """Определяет тип ввода и возвращает steamid64"""
    user_input = user_input.strip()

    # Просто steamid64
    if user_input.isdigit() and len(user_input) > 15:
        return int(user_input)

    # Ссылка: https://steamcommunity.com/profiles/7656119...
    if "steamcommunity.com/profiles/" in user_input:
        match = re.search(r'/profiles/(\d{17})', user_input)
        if match:
            return int(match.group(1))
        else:
            raise ValueError("Не удалось извлечь Steam ID из ссылки")

    # Ссылка: https://steamcommunity.com/id/имя
    if "steamcommunity.com/id/" in user_input:
        match = re.search(r'/id/([^/]+)/?', user_input)
        if match:
            vantity_name = match.group(1)
            steamid_64 = resolve_vanity_name(vantity_name)
            return steamid_64
        else:
            raise ValueError("Не удалось извлечь vanity name из ссылки")

    raise ValueError("Проверьте ввод, не удалось найти информацию по-данному пользователю")

def resolve_vanity_name(vanity: str) -> int:
    url = "https://api.steampowered.com/ISteamUser/ResolveVanityURL/v1/"
    params = {
        "key": STEAM_API_KEY,
        "vanityurl": vanity
    }
    response = requests.get(url, params=params).json()
    if response["response"]["success"] != 1:
        raise Exception("Пользователь не найден по vanity name")
    return int(response["response"]["steamid"])
