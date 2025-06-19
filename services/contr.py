# services/contr.py

from dota_api.heroes import *

hero_dict = get_hero_dict()
name_to_id = {name.lower(): hid for hid, name in hero_dict.items()}  # удобство поиска по имени

def build_counters_summary(hero_name_input: str) -> str:
    resolved_name = resolve_hero_name(hero_name_input)
    if not resolved_name:
        return "Герой не найден. Проверь имя или сокращение и попробуй ещё раз."

    hero_id = name_to_id.get(resolved_name)
    if not hero_id:
        return "Герой не найден в базе."

    matchups = get_hero_matchups(hero_id)

    for m in matchups:
        games = m["games_played"]
        wins = m["wins"]
        m["winrate"] = 100 - (wins / games * 100) if games else 0

    sorted_matchups = sorted(matchups, key=lambda x: x["winrate"], reverse=True)
    top_counters = sorted_matchups[:5]

    lines = []
    for m in top_counters:
        counter_hero_id = m["hero_id"]
        name = hero_dict.get(counter_hero_id, f"ID {counter_hero_id}").title()
        winrate = round(m["winrate"])
        emoji = pick_emoji(name)
        lines.append(f"{emoji} {name} — {winrate}% WR")

    header = f"Контрпики против {hero_dict[hero_id].title()}:"
    footer = "на основе данных последней недели"

    return f"{header}\n" + "\n".join(lines) + f"\n{footer}"