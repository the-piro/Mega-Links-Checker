import re
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from xtra import check_cmd, LINK_REGEX

WELCOME = "Hello {first}! Send me any MEGA link and I will check it."
IMG = "https://envs.sh/xLo.jpg/HGBOTZ.jpg"
MSG_EFFECT = 2  

btns = InlineKeyboardMarkup(
    [[InlineKeyboardButton("Repo", url="https://github.com/XalFH/Mega-Links-Checker")]]
)

@Client.on_message((filters.text | filters.caption) & ~filters.command(["start"]))
async def auto_check_mega(client, message):
    text = message.text or message.caption or ""
    if not re.search(LINK_REGEX, text):
        return
    await check_cmd(client, message)

@Client.on_message(filters.command("start"))
async def start_cmd(client, message):
    first_name = message.from_user.first_name if message.from_user else "there"
    username = f"@{message.from_user.username}" if getattr(message.from_user, "username", None) else ""
    
    start_caption = WELCOME.format(first=first_name)
    if username:
        start_caption += f"\n{username}"

    await client.send_photo(
        chat_id=message.chat.id,
        photo=IMG,
        caption=start_caption,
        message_effect_id=MSG_EFFECT,
        reply_markup=btns
    )
