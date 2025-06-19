from dota_api.heroes import *

hero_dict = get_hero_dict()
name_to_id = {name.lower(): hid for hid, name in hero_dict.items()}

def build_hero_about_summary(hero_name_input: str) -> str:
    resolved_name = resolve_hero_name(hero_name_input)
    if not resolved_name:
        return "Герой не найден. Проверь имя и попробуй снова."

    hero_id = name_to_id.get(resolved_name)
    if not hero_id:
        return "Герой не найден в базе."

    stats = get_hero_stats(hero_id)  # ты можешь реализовать это в своем `dota_api.heroes`
    if not stats:
        return "Не удалось получить данные по герою."

    name = hero_dict.get(hero_id, resolved_name).title()
    emoji = pick_emoji(name)

    return (
        f"{emoji} *{name}*\n\n"
        f"• Роль: {stats.get('roles', ['—'])}\n"
        #f"• Сложность: {stats.get('complexity', '—')}\n"
        f"• Winrate: {stats.get('winrate', '—')}%\n"
        f"• Частота выбора: {stats.get('pick_rate', '—')}%\n"
    )
