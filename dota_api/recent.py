# dota_api/recent.py

import requests

def get_last_matches(account_id: int, count: int = 10) -> list[dict]:
    url = f"https://api.opendota.com/api/players/{account_id}/matches"
    params = {"limit": count}

    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    return data  # список матчей (каждый — dict)
