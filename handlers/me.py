from aiogram import types
from aiogram.utils.markdown import escape_md

from database.db import get_user_steam_id


async def cmd_me(message: types.Message):
    telegram_id = message.from_user.id
    steam_id = await get_user_steam_id(telegram_id)

    # Данные из Telegram
    username = message.from_user.username or "—"
    full_name = message.from_user.full_name or "—"
    mention = message.from_user.mention or "—"

    if steam_id:
        response = (
            f"👤 *Информация о пользователе:*\n"
            f"• *Имя:* {escape_md(full_name)}\n"
            f"• *Username:* @{escape_md(username)}\n"
            f"• *Telegram ID:* `{telegram_id}`\n"
            f"• *Ссылка:* {mention}\n"
            f"• *Статус:* ✅ Зарегистрирован\n"
            f"• *Steam ID:* `{steam_id}`"
        )
    else:
        response = (
            f"👤 *Информация о пользователе:*\n"
            f"• *Имя:* {escape_md(full_name)}\n"
            f"• *Username:* @{escape_md(username)}\n"
            f"• *Telegram ID:* `{telegram_id}`\n"
            f"• *Ссылка:* {mention}\n"
            f"• *Статус:* ❌ Не зарегистрирован"
        )

    await message.answer(response, parse_mode="Markdown")
