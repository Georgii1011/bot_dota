# services/druft.py

from dota_api.meta import *
from utils.name_heroes import *

def build_meta_summary(limit=10):
    heroes = get_meta_heroes(limit)
    lines = []

    for hero in heroes:
        emoji = pick_emoji(hero["name"])
        lines.append(
            f"{emoji} {hero['name']} — {hero['winrate']}% WR | {hero['pickrate']}% PR"
        )
    return "🔥 Самые популярные герои сейчас:\n" + "\n".join(lines)