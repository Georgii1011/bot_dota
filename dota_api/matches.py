# dota_api/last.py

import requests

def get_last_match(account_id: int):
    url = f"https://api.opendota.com/api/players/{account_id}/matches"
    params = {"limit": 1}

    response = requests.get(url, params=params)

    data = response.json()

    if not data:
        return None
    return data[0]

def get_match_details(match_id: int) -> dict:
    url = f"https://api.opendota.com/api/matches/{match_id}"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"OpenDota вернул ошибку: {response.status_code}")

    try:
        return response.json()
    except ValueError:
        raise Exception(f"Пустой или некорректный JSON от OpenDota: {response.text}")