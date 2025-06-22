# services/recent.py

from dota_api.recent import *
from services.matches import *
from dota_api.heroes import *


async def build_recent_matches_summary(account_id: int, count: int = 10) -> str:
    matches = get_last_matches(account_id, count)
    if not matches:
        return "⚠️ Не удалось получить последние матчи."

    lines = []
    for match in matches:
        match_id = match["match_id"]
        match_data = get_match_details(match_id)

        try:
            summary = extract_match_summary(match_data, account_id)
        except Exception:
            continue

        hero = summary["hero"]
        result = "✅ Победа" if summary["win"] else "❌ Поражение"
        emoji = pick_emoji(hero)
        kda = f"{summary['kills']}/{summary['deaths']}/{summary['assists']}"
        date = summary["date"].strftime("%d.%m.%Y %H:%M")
        networth = summary.get("net_worth", "N/A")
        match_time = format_duration(match_data.get("duration", 0))

        lines.append(
            f"{emoji}{hero} — {result}\nK/D/A: {kda}\nДата: {date}\nNet Worth: {networth}\nВремя матча - {match_time}\n\n"
        )

    return "\n".join(lines)

def extract_match_summary(match_data: dict, account_id: int) -> dict:
    # Найдём игрока в матче
    player = None
    for p in match_data.get("players", []):
        if p.get("account_id") == account_id:
            player = p
            break
    if not player:
        raise ValueError("Игрок с таким account_id не найден в матче")

    hero_id = player.get("hero_id")
    hero_name = hero_dict.get(hero_id, "Unknown Hero")

    win = (player.get("win") == 1)

    kills = player.get("kills", 0)
    deaths = player.get("deaths", 0)
    assists = player.get("assists", 0)

    start_time = match_data.get("start_time", 0)
    from datetime import datetime
    match_datetime = datetime.fromtimestamp(start_time)

    net_worth = player.get("net_worth", "N/A")

    return {
        "hero": hero_name,
        "win": win,
        "kills": kills,
        "deaths": deaths,
        "assists": assists,
        "date": match_datetime,
        "net_worth": net_worth,
    }

