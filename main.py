from bot import Bot
from pyrogram import idle

try:
    Bot.loop.run_until_complete(Bot.get_me())
    idle()
except:
    Bot.stop()
