# services/about_hero.py

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

    stats = get_hero_stats(hero_id)
    if not stats:
        return "Не удалось получить данные по герою."

    name = hero_dict.get(hero_id, resolved_name).title()
    emoji = pick_emoji(name)

    # Формируем строку со всеми интересными данными
    return (
        f"{emoji} <b>{name}</b>\n\n"
        f"<b>Основной атрибут:</b> {attr_translate(stats['primary_attr'])}\n"
        f"<b>Тип атаки:</b> {stats['attack_type']}\n"
        f"<b>Роли:</b> {', '.join(stats.get('roles', []))}\n\n"

        f"<b>Характеристики:</b>\n"
        f"• Урон: {stats['base_attack_min']}–{stats['base_attack_max']}\n"
        f"• Атака каждые: {stats['attack_rate']} сек\n"
        f"• Броня: {stats['base_armor']}\n"
        f"• Дальность атаки: {stats['attack_range']} ед.\n"
        f"• Скорость передвижения: {stats['move_speed']} ед.\n\n"

        f"<b>Здоровье и мана:</b>\n"
        f"• Здоровье: {stats['base_health']} (+{stats['base_health_regen']}/с)\n"
        f"• Мана: {stats['base_mana']} (+{stats['base_mana_regen']}/с)\n\n"

        f"<b>Атрибуты:</b>\n"
        f"• Сила: {stats['base_str']} (+{stats['str_gain']})\n"
        f"• Ловкость: {stats['base_agi']} (+{stats['agi_gain']})\n"
        f"• Интеллект: {stats['base_int']} (+{stats['int_gain']})\n\n"

        f"<b>Статистика:</b>\n"
        f"• Winrate: {stats['winrate']}%\n"
        f"• Частота выбора (pro): {stats['pick_rate']}%\n"
    )

def attr_translate(attr: str) -> str:
    match attr:
        case "str": return "Сила"
        case "agi": return "Ловкость"
        case "int": return "Интеллект"
        case _: return "Неизвестно"

