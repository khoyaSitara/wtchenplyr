# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]

from pyrogram import filters
from pyrogram.types import Message

from WebStreamer.vars import Var 
from WebStreamer.bot import StreamBot

@StreamBot.on_message(filters.command(["start"]) & filters.private)
async def start(_, m: Message):
    if Var.ALLOWED_USERS and not ((str(m.from_user.id) in Var.ALLOWED_USERS) or (m.from_user.username in Var.ALLOWED_USERS)):
        return await m.reply(
            "You are not in the allowed list of users who can use me. \
            Check <a href='https://telegram.me/eliteflix_official'>this link</a> for more info.",
            disable_web_page_preview=True, quote=True
        )
    await m.reply(
        "<i>Hi Boi</i>\n<i>Im  Download Link Generator Bot 📥</i>\n<i>Use /help command For More Info</i>\n<i><u>Warning ⚠️</u></i><b>🔞 Poem Contents Lead To Ban.</b>\n\n <i><b>👑 Bot Maintained By :</b>@Ashishsharmalegend</i>"
    )
    

@StreamBot.on_message(filters.command(["help"]) & filters.private)
async def start(_, m: Message):
    if Var.ALLOWED_USERS and not ((str(m.from_user.id) in Var.ALLOWED_USERS) or (m.from_user.username in Var.ALLOWED_USERS)):
        return await m.reply(
            "You are not in the allowed list of users who can use me. \
            Check <a href='https://telegram.me/eliteflix_official'>this link</a> for more info.",
            disable_web_page_preview=True, quote=True
        )
    await m.reply(
        "<i>- Send Me Any File Or Media For Telegram.</i>\n <i>- I Will Provide External Direct Download Link !.</i>\n <i>- Add Me In Your Channel For Direct Download Link Button</i> <i>- Generate The Permanent Link With Fastest Speed</i>\n <i>- You Can Use This Link To Stream File Online Without Downloading In Your Media Player.</i>\n <u>🔸 Warning ⚠️</u>\n <b>🔞 Poem Contents Lead To Ban.</b>\n <i>Contact Owner / Report Error/Bugs</i> <b>: <a href='https://t.me/Ashishsharmalegend'>[ Click Here ]</a></b>"
    )

@StreamBot.on_message(filters.command(["about"]) & filters.private)
async def start(_, m: Message):
    if Var.ALLOWED_USERS and not ((str(m.from_user.id) in Var.ALLOWED_USERS) or (m.from_user.username in Var.ALLOWED_USERS)):
        return await m.reply(
            "You are not in the allowed list of users who can use me. \
            Check <a href='https://telegram.me/eliteflix_official'>this link</a> for more info.",
            disable_web_page_preview=True, quote=True
        )
    await m.reply(
        "<b>🙋My Name : Eliteflix File To Link Bot</b>\n <b>🚲Bot Version : <a href='https://telegram.me/eliteflix_official'>1.2.8</a></b>\n <b>👑Owner/Developer : <a href='https://telegram.me/Ashishsharmalegend'>Ansh Kummar</a></b>\n <b>🧑‍💻Last Updated : <a href='https://telegram.me/eliteflix_official'>[ 25 - Oct - 2023 ] 10:28 pm</a></b>\n <b>🥺Repo : <a href='https://telegram.me/Ashishsharmalegend'>Soo Ja Nhi Milega 😂😂</a></b>\n"
    )
