def rank_tier_to_str(rank_tier: int | None) -> str:
    if not rank_tier:
        return "Нет данных"

    tiers = ["Herald", "Guardian", "Crusader", "Archon", "Legend", "Ancient", "Divine", "Immortal"]
    div = rank_tier % 10
    tier = rank_tier // 10

    if tier == 8:
        return "Immortal"
    if 1 <= tier <= 7:
        div_map = {0: "0", 1: "5", 2: "4", 3: "3", 4: "2", 5: "1"}
        return f"{tiers[tier - 1]} {div}"
    return "Неизвестный ранг"
