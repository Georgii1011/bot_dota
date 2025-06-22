# keyboards/menu.py

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_main_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row(
        KeyboardButton("📊 Общие"),
        KeyboardButton("📅 Матчи")
    )
    kb.row(
        KeyboardButton("🙋 Игроку"),
        KeyboardButton("🦸 Герои")
    )
    kb.row(
        KeyboardButton("🎯 Драфт"),
        KeyboardButton("⚖️ Сравнение")
    )
    kb.row(
        KeyboardButton("🎉 Фан")
    )

    return kb

def get_common_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row(
        KeyboardButton("👋🤖 Привествие или обновление бота"),
        KeyboardButton("ℹ️ Помощь")
    )
    kb.row(
        KeyboardButton("🧾 Установить Steam ID"),
        KeyboardButton("ℹ️ Информация обо мне")
    )
    kb.row(
        KeyboardButton("🚀 Планы на будущее"),
        KeyboardButton("🔙 Назад")
    )

    return kb

def get_matches_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row(
        KeyboardButton("📊 Последняя игра"),
        KeyboardButton("🎮 Последние игры")
    )
    kb.row(
        KeyboardButton("🔙 Назад")
    )

    return kb

def get_player_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row(
        KeyboardButton("📈 Моя статистика")
    )
    kb.row(
        KeyboardButton("🔙 Назад")
    )

    return kb

def get_heroes_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row(
        KeyboardButton("🛡 Контрпики")
    )
    kb.row(
        KeyboardButton("🔙 Назад")
    )

    return kb

def get_meta_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row(
        KeyboardButton("🔥 Лучшие герои")
    )
    kb.row(
        KeyboardButton("🔙 Назад")
    )

    return kb

def get_comprasion_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row(
        KeyboardButton("🔙 Назад")
    )

    return kb

def get_fun_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row(
        KeyboardButton("🔙 Назад")
    )

    return kb

def get_numbers_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row(
        KeyboardButton("1"),
        KeyboardButton("2"),
        KeyboardButton("3"),
        KeyboardButton("4"),
        KeyboardButton("5"),
    )
    kb.row(
        KeyboardButton("6"),
        KeyboardButton("7"),
        KeyboardButton("8"),
        KeyboardButton("9"),
        KeyboardButton("10")
    )
    kb.row(
        KeyboardButton("🔙 Назад")
    )

    return kb


def get_listofheroes_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row(
        KeyboardButton("Abaddon"), KeyboardButton("Alchemist"),
        KeyboardButton("Ancient Apparition"), KeyboardButton("Anti-Mage"),
        KeyboardButton("Arc Warden"), KeyboardButton("Axe")
    )
    kb.row(
        KeyboardButton("Bane"), KeyboardButton("Batrider"),
        KeyboardButton("Beastmaster"), KeyboardButton("Bloodseeker"),
        KeyboardButton("Bounty Hunter"), KeyboardButton("Brewmaster")
    )
    kb.row(
        KeyboardButton("Bristleback"), KeyboardButton("Broodmother"),
        KeyboardButton("Centaur Warrunner"), KeyboardButton("Chaos Knight"),
        KeyboardButton("Chen"), KeyboardButton("Clinkz")
    )
    kb.row(
        KeyboardButton("Clockwerk"), KeyboardButton("Crystal Maiden"),
        KeyboardButton("Dark Seer"), KeyboardButton("Dark Willow"),
        KeyboardButton("Dawnbreaker"), KeyboardButton("Dazzle")
    )
    kb.row(
        KeyboardButton("Death Prophet"), KeyboardButton("Disruptor"),
        KeyboardButton("Doom"), KeyboardButton("Dragon Knight"),
        KeyboardButton("Drow Ranger"), KeyboardButton("Earth Spirit")
    )
    kb.row(
        KeyboardButton("Earthshaker"), KeyboardButton("Elder Titan"),
        KeyboardButton("Ember Spirit"), KeyboardButton("Enchantress"),
        KeyboardButton("Enigma"), KeyboardButton("Faceless Void")
    )
    kb.row(
        KeyboardButton("Grimstroke"), KeyboardButton("Gyrocopter"),
        KeyboardButton("Hoodwink"), KeyboardButton("Huskar"),
        KeyboardButton("Invoker"), KeyboardButton("Io")
    )
    kb.row(
        KeyboardButton("Jakiro"), KeyboardButton("Juggernaut"),
        KeyboardButton("Keeper of the Light"), KeyboardButton("Kez"),
        KeyboardButton("Kunkka"), KeyboardButton("Legion Commander")
    )
    kb.row(
        KeyboardButton("Leshrac"), KeyboardButton("Lich"),
        KeyboardButton("Lifestealer"), KeyboardButton("Lina"),
        KeyboardButton("Lion"), KeyboardButton("Lone Druid")
    )
    kb.row(
        KeyboardButton("Luna"), KeyboardButton("Lycan"),
        KeyboardButton("Magnus"),KeyboardButton("Marci"),
        KeyboardButton("Mars"), KeyboardButton("Medusa")
    )
    kb.row(
        KeyboardButton("Meepo"), KeyboardButton("Mirana"),
        KeyboardButton("Monkey King"), KeyboardButton("Morphling"),
        KeyboardButton("Muerta"), KeyboardButton("Naga Siren")
    )
    kb.row(
        KeyboardButton("Nature's Prophet"), KeyboardButton("Necrophos"),
        KeyboardButton("Night Stalker"), KeyboardButton("Nyx Assassin"),
        KeyboardButton("Ogre Magi"), KeyboardButton("Omniknight")
    )
    kb.row(
        KeyboardButton("Oracle"), KeyboardButton("Outworld Destroyer"),
        KeyboardButton("Pangolier"), KeyboardButton("Phantom Assassin"),
        KeyboardButton("Phantom Lancer"), KeyboardButton("Phoenix")
    )
    kb.row(
        KeyboardButton("Primal Beast"), KeyboardButton("Puck"),
        KeyboardButton("Pudge"), KeyboardButton("Pugna"),
        KeyboardButton("Queen of Pain"), KeyboardButton("Razor")
    )
    kb.row(
        KeyboardButton("Riki"), KeyboardButton("Ringmaster"),
        KeyboardButton("Rubick"), KeyboardButton("Sand King"),
        KeyboardButton("Shadow Demon"), KeyboardButton("Shadow Fiend"),
    )
    kb.row(
        KeyboardButton("Shadow Shaman"), KeyboardButton("Silencer"),
        KeyboardButton("Skywrath Mage"), KeyboardButton("Slardar"),
        KeyboardButton("Slark"), KeyboardButton("Snapfire"),

    )
    kb.row(
        KeyboardButton("Sniper"), KeyboardButton("Spectre"),
        KeyboardButton("Spirit Breaker"), KeyboardButton("Storm Spirit"),
        KeyboardButton("Sven"), KeyboardButton("Techies"),

    )
    kb.row(
        KeyboardButton("Templar Assassin"), KeyboardButton("Terrorblade"),
        KeyboardButton("Tidehunter"), KeyboardButton("Timbersaw"),
        KeyboardButton("Tinker"), KeyboardButton("Tiny"),
    )
    kb.row(
        KeyboardButton("Treant Protector"), KeyboardButton("Troll Warlord"),
        KeyboardButton("Tusk"), KeyboardButton("Underlord"),
        KeyboardButton("Undying"), KeyboardButton("Ursa"),

    )
    kb.row(
        KeyboardButton("Vengeful Spirit"), KeyboardButton("Venomancer"),
        KeyboardButton("Viper"), KeyboardButton("Visage"),
        KeyboardButton("Void Spirit"), KeyboardButton("Warlock"),
    )
    kb.row(
        KeyboardButton("Weaver"), KeyboardButton("Windranger"),
        KeyboardButton("Winter Wyvern"), KeyboardButton("Witch Doctor"),
        KeyboardButton("Wraith King"), KeyboardButton("Zeus")
    )
    kb.row(
        KeyboardButton("🔙 Назад")
    )

    return kb