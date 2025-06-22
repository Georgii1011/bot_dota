# services/player.py

from dota_api.player import *
from services.rank_tier import *


def format_player_stats_message(steam_input: str, account_id: int) -> str:
    stats = get_player_winloss(account_id)

    wins = stats["wins"]
    losses = stats["losses"]
    total = wins + losses
    winrate = round((wins / total) * 100, 2) if total > 0 else 0.0

    rank_info = get_player_rank(account_id)
    rank_str = rank_tier_to_str(rank_info.get("rank_tier"))
    leaderboard = rank_info.get("leaderboard_rank")
    leaderboard_str = f"\n🏅 Место в рейтинге: {leaderboard}" if leaderboard else ""

    return (
        f"📘 Твой профиль: `{steam_input}`\n\n"
        f"🏆 Победы: {wins}\n"
        f"💀 Поражения: {losses}\n"
        f"📊 Винрейт: {winrate}%\n"
        f"🧩 Всего матчей: {total}\n"
        f"🎖 Примерный ранг: {rank_str}"
        f"{leaderboard_str}"
    )