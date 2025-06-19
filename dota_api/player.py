# dota_api/player.py

import requests

def get_player_winloss(account_id: int) -> dict:
    url = f"https://api.opendota.com/api/players/{account_id}/wl"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Не удалось получить статистику игрока с OpenDota")

    data = response.json()
    return {
        "wins": data.get("win", 0),
        "losses": data.get("lose", 0),
    }

import requests

def get_player_rank(account_id: int) -> dict:
    """
    Возвращает словарь с рангом и местом в рейтинге (если есть).
    """
    try:
        url = f"https://api.opendota.com/api/players/{account_id}"
        resp = requests.get(url)
        resp.raise_for_status()
        data = resp.json()

        rank_tier = data.get("rank_tier")  # Пример: 70, 80 и т.п.
        leaderboard_rank = data.get("leaderboard_rank")  # Может быть None

        return {
            "rank_tier": rank_tier,
            "leaderboard_rank": leaderboard_rank,
        }
    except Exception as e:
        print(f"Ошибка при получении ранга игрока: {e}")
        return {
            "rank_tier": None,
            "leaderboard_rank": None,
        }
