@Client.on_message(filters.text | filters.caption)
async def auto_check_mega(client, message):
    if message.text and message.text.startswith("/start"):
        return

    text = message.text or message.caption or ""
    if not re.search(LINK_REGEX, text):
        return

    await check_cmd(client, message)


@Client.on_message(filters.command("start"))
async def start_cmd(client, message):
    await message.reply_text(WELCOME, quote=True)
