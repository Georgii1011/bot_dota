# services/last.py

from dota_api.heroes import *
from dota_api.matches import *
from utils.name_heroes import *
from datetime import timedelta

hero_dict = get_hero_dict()

def format_duration(seconds: int) -> str:
    return str(timedelta(seconds=seconds))[2:7]  # мм:сс


def build_match_summary(account_id: int) -> str:
    match = get_last_match(account_id)
    if not match:
        return "Матчей не найдено. Возможно, профиль скрыт."

    match_id = match["match_id"]
    hero_id = match["hero_id"]
    player_hero_name = hero_dict.get(hero_id, f"ID {hero_id}")

    match_details = get_match_details(match_id)
    players = match_details.get("players", [])

    radiant_win = match_details.get("radiant_win")
    winner = "Radiant 🟢 победили!" if radiant_win else "Dire 🔴 победили!"

    match_time = format_duration(match_details.get("duration", 0))

    radiant_heroes = []
    dire_heroes = []

    for player in players:
        hid = player["hero_id"]
        name = hero_dict.get(hid, f"ID {hid}")
        emoji = pick_emoji(name)

        kills = player.get("kills", 0)
        deaths = player.get("deaths", 0)
        assists = player.get("assists", 0)
        networth = player.get("total_gold", 0)
        net_str = f"NET: {networth}"

        player_account_id = player.get("account_id")
        is_you = player_account_id is not None and player_account_id == account_id
        you_tag = " (ты)" if is_you else ""

        line = f"• {emoji} {name}{you_tag} — {kills}/{deaths}/{assists}, {net_str}"

        if player["isRadiant"]:
            radiant_heroes.append(line)
        else:
            dire_heroes.append(line)

    return (
        f"🕹 Последний матч: {match_id}\n"
        f"⏱ Длительность: {match_time}\n"
        f"Ты играл за: {player_hero_name}\n"
        f"{winner}\n\n"
        f"🟢 Radiant:\n" + "\n".join(radiant_heroes) +
        f"\n\n🔴 Dire:\n" + "\n".join(dire_heroes)
    )
