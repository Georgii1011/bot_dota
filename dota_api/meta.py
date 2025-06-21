# dota_api/druft.py

import requests

def get_meta_heroes(limit=10, sort_by="winrate", reverse=True):
    url = "https://api.opendota.com/api/heroStats"
    response = requests.get(url)
    data = response.json()

    total_pro_games = sum(hero.get("pro_pick", 0) for hero in data)

    result = []

    for hero in data:
        name = hero["localized_name"]
        picks = hero.get("pro_pick", 0)
        wins = hero.get("pro_win", 0)
        bans = hero.get("pro_ban", 0)

        pickrate = round((picks / total_pro_games) * 100, 1) if total_pro_games else 0
        winrate = round((wins / picks) * 100, 1) if picks else 0
        banrate = round((bans / total_pro_games) * 100, 1) if total_pro_games else 0

        result.append({
            "name": name,
            "winrate": winrate,
            "pickrate": pickrate,
            "banrate": banrate
        })

    # Защита от неправильного sort_by
    if sort_by not in ["pickrate", "winrate", "banrate"]:
        sort_by = "winrate"

    sorted_result = sorted(result, key=lambda h: h[sort_by], reverse=reverse)
    return sorted_result[:limit]


