# utils/name_heroes.py

def pick_emoji(name: str) -> str:
    name = name.lower()
    if any(h in name for h in ["axe", "centaur", "underlord", "bristleback"]):
        return "🛡"  # Танки
    if any(h in name for h in ["legion", "sven", "wraith", "mars"]):
        return "🔥"  # Воины, фронтлайн
    if any(h in name for h in ["lich", "ancient", "crystal", "kotl", "pugna", "grim", "dazzle", "chen", "oracle", "shadow", "warlock", "enchantress", "wyvern"]):
        return "🧊"  # Маги/саппорты
    if any(h in name for h in ["phantom", "riki", "bounty", "slark", "clinkz", "naga", "mirana", "wind", "templar", "drow"]):
        return "🎯"  # Ловкачи
    if any(h in name for h in ["earthshaker", "magnus", "tiny", "sand", "dark seer", "enigma", "tide"]):
        return "🌋"  # Контроль, инициаторы
    if any(h in name for h in ["invoker", "storm", "zeus", "tinker", "leshrac", "skywrath", "lina", "lion"]):
        return "⚡"  # Мощные маги
    if any(h in name for h in ["juggernaut", "pa", "terrorblade", "ursa", "lifestealer", "monkey", "anti", "spectre", "faceless"]):
        return "🗡"  # Керри
    if any(h in name for h in ["brood", "meepo", "arc", "visage", "beast", "lone", "lycan"]):
        return "🕷"  # Призыватели/зоолидеры
    if any(h in name for h in ["techies", "clock", "tinker", "batrider", "timbersaw"]):
        return "🛠"  # Инженеры, устройства
    if any(h in name for h in ["death", "necrophos", "doom", "abaddon", "terror", "venge", "undying"]):
        return "💀"  # Темные герои

    return "✨"  # По умолчанию

aliases = {
"anti-mage": "anti-mage",
    "axe": "axe",
    "bane": "bane",
    "bloodseeker": "bloodseeker",
    "crystal maiden": "crystal maiden",
    "drow ranger": "drow ranger",
    "earthshaker": "earthshaker",
    "juggernaut": "juggernaut",
    "mirana": "mirana",
    "morphling": "morphling",
    "nevermore": "nevermore",
    "phantom lancer": "phantom lancer",
    "puck": "puck",
    "pudge": "pudge",
    "razor": "razor",
    "sand king": "sand king",
    "storm spirit": "storm spirit",
    "sven": "sven",
    "tiny": "tiny",
    "vengeful spirit": "vengeful spirit",
    "windranger": "windranger",
    "zuus": "zuus",
    "kunkka": "kunkka",
    "lich": "lich",
    "riki": "riki",
    "enigma": "enigma",
    "tinker": "tinker",
    "sniper": "sniper",
    "necrolyte": "necrolyte",
    "warlock": "warlock",
    "beastmaster": "beastmaster",
    "queen of pain": "queen of pain",
    "venomancer": "venomancer",
    "faceless void": "faceless void",
    "skeleton king": "skeleton king",
    "death prophet": "death prophet",
    "phantom assassin": "phantom assassin",
    "pugna": "pugna",
    "templar assassin": "templar assassin",
    "viper": "viper",
    "luna": "luna",
    "dragon knight": "dragon knight",
    "dazzle": "dazzle",
    "clockwerk": "clockwerk",
    "leshrac": "leshrac",
    "nature's prophet": "nature's prophet",
    "lifestealer": "lifestealer",
    "dark seer": "dark seer",
    "clinkz": "clinkz",
    "omniknight": "omniknight",
    "enchantress": "enchantress",
    "huskar": "huskar",
    "night stalker": "night stalker",
    "broodmother": "broodmother",
    "bounty hunter": "bounty hunter",
    "weaver": "weaver",
    "jakiro": "jakiro",
    "batrider": "batrider",
    "chen": "chen",
    "spectre": "spectre",
    "doom": "doom",
    "ancient apparition": "ancient apparition",
    "ursa": "ursa",
    "spirit breaker": "spirit breaker",
    "gyrocopter": "gyrocopter",
    "alchemist": "alchemist",
    "invoker": "invoker",
    "silencer": "silencer",
    "obsidian destroyer": "obsidian destroyer",
    "lycan": "lycan",
    "brewmaster": "brewmaster",
    "shadow demon": "shadow demon",
    "lone druid": "lone druid",
    "chaos knight": "chaos knight",
    "meepo": "meepo",
    "treant protector": "treant protector",
    "ogre magi": "ogre magi",
    "undying": "undying",
    "rubick": "rubick",
    "disruptor": "disruptor",
    "nyx assassin": "nyx assassin",
    "naga siren": "naga siren",
    "keeper of the light": "keeper of the light",
    "wisp": "wisp",
    "visage": "visage",
    "slardar": "slardar",
    "tidal warrior": "tidal warrior",
    "slark": "slark",
    "medusa": "medusa",
    "troll warlord": "troll warlord",
    "centaur warrunner": "centaur warrunner",
    "magnus": "magnus",
    "timbersaw": "timbersaw",
    "bristleback": "bristleback",
    "tusk": "tusk",
    "skywrath mage": "skywrath mage",
    "abaddon": "abaddon",
    "elder titan": "elder titan",
    "legion commander": "legion commander",
    "techies": "techies",
    "ember spirit": "ember spirit",
    "earth spirit": "earth spirit",
    "underlord": "underlord",
    "terrorblade": "terrorblade",
    "phoenix": "phoenix",
    "oracle": "oracle",
    "winter wyvern": "winter wyvern",
    "arc warden": "arc warden",
    "monkey king": "monkey king",
    "dark willow": "dark willow",
    "pangolier": "pangolier",
    "grimstroke": "grimstroke",
    "hoodwink": "hoodwink",
    "void spirit": "void spirit",
    "snapfire": "snapfire",
    "mars": "mars",
    "dawnbreaker": "dawnbreaker",
    "marci": "marci",

    # сокращения
    "aa": "ancient apparition",
    "alch": "alchemist",
    "am": "anti-mage",
    "antimage": "anti-mage",
    "arc": "arc warden",
    "bat": "batrider",
    "bb": "bristleback",
    "beast": "beastmaster",
    "bh": "bounty hunter",
    "bs": "bloodseeker",
    "brew": "brewmaster",
    "brood": "broodmother",
    "centaur": "centaur warrunner",
    "ck": "chaos knight",
    "clock": "clockwerk",
    "cm": "crystal maiden",
    "ds": "dark seer",
    "dw": "dark willow",
    "dp": "death prophet",
    "dk": "dragon knight",
    "drow": "drow ranger",
    "es": "earthshaker",
    "elder": "elder titan",
    "ember": "ember spirit",
    "void": "faceless void",
    "furion": "nature's prophet",
    "gyro": "gyrocopter",
    "io": "io",
    "jug": "juggernaut",
    "jugger": "juggernaut",
    "lc": "legion commander",
    "lesh": "leshrac",
    "lina": "lina",
    "lion": "lion",
    "lone": "lone druid",
    "loon": "lone druid",
    "loon druid": "lone druid",
    "mag": "magnus",
    "mk": "monkey king",
    "morph": "morphling",
    "muerta": "muerta",
    "naix": "lifestealer",
    "naga": "naga siren",
    "np": "nature's prophet",
    "ns": "night stalker",
    "nyx": "nyx assassin",
    "ogre": "ogre magi",
    "omni": "omniknight",
    "od": "outworld destroyer",
    "pango": "pangolier",
    "pa": "phantom assassin",
    "pl": "phantom lancer",
    "qop": "queen of pain",
    "sh": "shadow shaman",
    "shaman": "shadow shaman",
    "shadow fiend": "nevermore",
    "sf": "nevermore",
    "sky": "skywrath mage",
    "snap": "snapfire",
    "storm": "storm spirit",
    "ta": "templar assassin",
    "tb": "terrorblade",
    "tide": "tidehunter",
    "timber": "timbersaw",
    "treant": "treant protector",
    "troll": "troll warlord",
    "venge": "vengeful spirit",
    "veno": "venomancer",
    "wd": "witch doctor",
    "wind": "windranger",
    "wr": "windranger",
    "winter": "winter wyvern",
    "ww": "winter wyvern",
    "wk": "wraith king",
    "zeus": "zeus",

    #русский
    "хуесос": "viper",
    "сын шлюхи": "tinker",
    "абхадон": "abaddon",
    "бабадон": "abaddon",
    "алхим": "alchemist",
    "антимаг": "anti‑mage",
    "акс": "axe",
    "бейнд": "bane",
    "бэтик": "batrider",
    "рексар": "beastmaster",
    "бс": "bloodseeker",
    "бх": "bounty hunter",
    "панда": "brewmaster",
    "брист": "bristleback",
    "бруда": "broodmother",
    "кентавр": "centaur warrunner",
    "чан": "chen",
    "клинкз": "clinkz",
    "клок": "clockwerk",
    "цм": "crystal maiden",
    "вейла": "dark willow",
    "даун": "dawnbreaker",
    "дазл": "dazzle",
    "баньша": "death prophet",
    "дизраптор": "disruptor",
    "дум": "doom",
    "дк": "dragon knight",
    "дровка": "drow ranger",
    "земля": "earth spirit",
    "шейкер": "earthshaker",
    "титан": "elder titan",
    "эмбер": "ember spirit",
    "энча": "enchantress",
    "энигма": "enigma",
    "воид": "faceless void",
    "гиро": "gyrocopter",
    "худвинк": "hoodwink",
    "хускар": "huskar",
    "инвок": "invoker",
    "ио": "io",
    "джокер": "jakiro",
    "джагер": "juggernaut",
    "котл": "keeper of the light",
    "кунка": "kunkka",
    "лк": "legion commander",
    "леший": "leshrac",
    "лич": "lich",
    "гуля": "lifestealer",
    "лина": "lina",
    "лион": "lion",
    "друид": "lone druid",
    "луна": "luna",
    "ликан": "lycan",
    "магнус": "magnus",
    "марс": "mars",
    "медуза": "medusa",
    "мипо": "meepo",
    "мирена": "mirana",
    "мк": "monkey king",
    "морф": "morphling",
    "муэрта": "muerta",
    "нга": "naga siren",
    "нпропет": "nature's prophet",
    "нс": "night stalker",
    "никс": "nyx assassin",
    "огр": "ogre magi",
    "омник": "omniknight",
    "оракл": "oracle",
    "од": "outworld destroyer",
    "панго": "pangolier",
    "фантомка": "phantom assassin",
    "пл": "phantom lancer",
    "пак": "puck",
    "пудж": "pudge",
    "пугна": "pugna",
    "квоп": "queen of pain",
    "разор": "razor",
    "рики": "riki",
    "руби́к": "rubick",
    "ск": "sand king",
    "шаман": "shadow shaman",
    "сф": "shadow fiend",
    "силенсер": "silencer",
    "скаймаг": "skywrath mage",
    "слардар": "slardar",
    "сларк": "slark",
    "снепка": "snapfire",
    "снайпер": "sniper",
    "спектра": "spectre",
    "спиритбрейкер": "spirit breaker",
    "батя" : "breaker",
    "шторм": "storm spirit",
    "свен": "sven",
    "та": "templar assassin",
    "тб": "terrorblade",
    "тайд": "tidehunter",
    "тимбер": "timbersaw",
    "тинкер": "tinker",
    "тини": "tiny",
    "трент": "treant protector",
    "тролль": "troll warlord",
    "туск": "tusk",
    "андер": "underlord",
    "урса": "ursa",
    "венга": "vengeful spirit",
    "веном": "venomancer",
    "вайпер": "viper",
    "визаж": "visage",
    "воидспирит": "void spirit",
    "варлок": "warlock",
    "вивер": "weaver",
    "вд": "witch doctor",
    "виндра": "windranger",
    "виверна": "winter wyvern",
    "вк": "wraith king",
    "зевс": "zeus"
    }

def get_hero_complexities() -> dict[int, int]:
    return {
        1: 3,    # Anti-Mage
        2: 2,    # Axe
        3: 3,    # Bane
        4: 2,    # Bloodseeker
        5: 2,    # Crystal Maiden
        6: 3,    # Drow Ranger
        7: 1,    # Earthshaker
        8: 2,    # Juggernaut
        9: 2,    # Mirana
        10: 3,   # Morphling
        11: 2,   # Shadow Fiend
        12: 3,   # Phantom Lancer
        13: 3,   # Puck
        14: 3,   # Pudge
        15: 1,   # Razor
        16: 3,   # Sand King
        17: 3,   # Storm Spirit
        18: 2,   # Sven
        19: 1,   # Tiny
        20: 3,   # Vengeful Spirit
        21: 2,   # Windranger
        22: 2,   # Zeus
        23: 1,   # Kunkka
        25: 1,   # Lina
        26: 2,   # Lion
        27: 2,   # Shadow Shaman
        28: 1,   # Slardar
        29: 3,   # Tidehunter
        30: 3,   # Witch Doctor
        31: 2,   # Lich
        32: 3,   # Riki
        33: 1,   # Enigma
        34: 2,   # Tinker
        35: 3,   # Sniper
        36: 1,   # Necrophos
        37: 2,   # Warlock
        38: 2,   # Beastmaster
        39: 2,   # Queen of Pain
        40: 3,   # Venomancer
        41: 1,   # Faceless Void
        42: 2,   # Wraith King
        43: 2,   # Death Prophet
        44: 2,   # Phantom Assassin
        45: 3,   # Pugna
        46: 2,   # Chaos Knight
        47: 2,   # Meepo
        48: 3,   # Treant Protector
        49: 3,   # Ogre Magi
        50: 2,   # Undying
        51: 2,   # Rubick
        52: 1,   # Disruptor
        53: 3,   # Nyx Assassin
        54: 3,   # Naga Siren
        55: 2,   # Keeper of the Light
        56: 2,   # Io
        57: 2,   # Visage
        58: 3,   # Slark
        59: 1,   # Medusa
        60: 3,   # Troll Warlord
        61: 2,   # Centaur Warrunner
        62: 2,   # Magnus
        63: 3,   # Timbersaw
        64: 3,   # Bristleback
        65: 1,   # Tusk
        66: 2,   # Skywrath Mage
        67: 3,   # Abaddon
        68: 2,   # Elder Titan
        69: 3,   # Legion Commander
        70: 2,   # Techies
        71: 2,   # Oracle
        72: 2,   # Winter Wyvern
        73: 3,   # Arc Warden
        74: 3,   # Monkey King
        75: 3,   # Dark Willow
        76: 3,   # Pangolier
        77: 2,   # Grimstroke
        78: 2,   # Hoodwink
        79: 2,   # Void Spirit
        80: 3,   # Snapfire
        81: 3,   # Mars
        82: 3,   # Dawnbreaker
        83: 3,   # Marci
        # Дополняй при необходимости для новых героев
    }