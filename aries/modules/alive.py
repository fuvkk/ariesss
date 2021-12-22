from telethon import Button

from aries import telethn as tbot
from aries.events import register

PHOTO = "https://telegra.ph/file/c20a6da05abc7a15297d1.jpg"


@register(pattern=("/alive|/ALIVE"))
async def awake(event):
    event.sender.first_name
    ARIES = "**Hello I'm Creator Pavan** \n\n"
    ARIES += "**ALL SYSTEM WORKING PROPERLY**\n\n"
    ARIES += " ⎇ **Python :** __3.9.7__ \n\n"
    ARIES += " ⎇ **Pyrogram :** __1.2.9__ \n\n"
    ARIES += " ⎇ **MongoDB :** __2.5.1__ \n\n"
    ARIES += " ⎇ **Platform :** __linux__ \n\n"
    ARIES += " ⎇ **My Lord** : [Creator Pavan](https://t.me/Creator_pavan)\n\n"
    ARIES += " ⎇ **Creator Pavan Robot**\n\n"
    ARIES += " ⎇ **TELETHON : 6.6.6 Latest**\n\n"
    ARIES += " |||| || ||| |||| || |||||| ||||| || || ||"
    BUTTON = [
        [
            Button.url("Support", "https://t.me/CreatorPavanSupport"),
            Button.url("Owner", "https://t.me/Creator_Pavan"),
        ]
    ]
    await tbot.send_file(event.chat_id, PHOTO, caption=ARIES, buttons=BUTTON)


__mod_name__ = "ᴀʟɪᴠᴇ"
