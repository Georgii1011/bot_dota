# services/heroes.py

def format_hero_info(hero_data: dict, complexity: int | None = None) -> str:
    name = hero_data.get("localized_name", "Неизвестный герой")
    primary_attr = hero_data.get("primary_attr", "-").capitalize()
    attack_type = hero_data.get("attack_type", "-")
    roles = hero_data.get("roles", [])
    roles_str = ", ".join(roles) if roles else "-"

    base_health = hero_data.get("base_health", 0)
    base_health_regen = hero_data.get("base_health_regen", 0)
    base_mana = hero_data.get("base_mana", 0)
    base_mana_regen = hero_data.get("base_mana_regen", 0)
    base_armor = hero_data.get("base_armor", 0)
    base_mr = hero_data.get("base_mr", 0)

    pub_pick = hero_data.get("pub_pick", 0)
    pub_win = hero_data.get("pub_win", 0)
    winrate = (pub_win / pub_pick * 100) if pub_pick else 0

    complexity_str = str(complexity) if complexity is not None else "-"

    info = (
        f"Герой: {name}\n"
        f"Атрибут: {primary_attr}\n"
        f"Тип атаки: {attack_type}\n"
        f"Роли: {roles_str}\n"
        f"Сложность: {complexity_str}\n\n"

        f"Базовые характеристики:\n"
        f"  Здоровье: {base_health} (+regen {base_health_regen})\n"
        f"  Мана: {base_mana} (+regen {base_mana_regen})\n"
        f"  Броня: {base_armor}\n"
        f"  Магический резист: {base_mr}%\n\n"

        f"Статистика (публичные игры):\n"
        f"  Пики: {pub_pick}\n"
        f"  Победы: {pub_win}\n"
        f"  Винрейт: {winrate:.2f}%\n"
    )

    return info
