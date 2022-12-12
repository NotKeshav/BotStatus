#Copyright ©️ 2021 TeLe TiPs. All Rights Reserved
#You are free to use this code in any of your project, but you MUST include the following in your README.md (Copy & paste)
# ##Credits - [BotStatus Telegram bot by TeLe TiPs] (https://github.com/teletips/Powerful_BotStatus-TeLeTiPs)

# Changing the code is not allowed! Read GNU AFFERO GENERAL PUBLIC LICENSE: https://github.com/teletips/Powerful_BotStatus-TeLeTiPs/blob/main/LICENSE

from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import asyncio
import datetime
import pytz
import os

app = Client(
    name = "botstatus_teletips",
    api_id = 13691707,
    api_hash = "2a31b117896c5c7da27c74025aa602b8",
    session_string = "BQBiMZkAryFRmnGGGDZKfmO544Fxy59EHt7F-HZ9FtBSooBTlecTbf8O6cK7wMjSLEM7WRChucWwk9Q9WK1pKkBuQ-flHUf4Ru7YGFhoOeNqEPAFn_Bvocqzc-LK0m16FdAeq8Y2gVwsAJoMuru4_O1DUJljec3E8P1aMuWgwB9NjUt00Hl9WKmrQejopcdBMTx8DPhinJ75_XFgISLO5PoVivvs1pb3FJtVr6cEnQcDDzigCbaeyt4-THXG5ha1hvie4bihC7QH07OLUcJb8-AqfXhCr9hsZAKz1DIZQ8KpxUPVJcsPKhjTkjS61WNaFOioZbUs3HV6Fj56-gM_OObYESiD7gAAAAE35sIdAA"
)
TIME_ZONE = "Asia/Kolkata"
BOT_LIST = ["Spl_Levi_Ackerman_Bot", "spl_afk_bot", "spl_sticker_bot"]
CHANNEL_OR_GROUP_ID = -1001401571895
MESSAGE_ID = 3
BOT_ADMIN_IDS = [5868832590, 5232837149]
PLATFORM = ["Vps", "Vps", "Vps"]

async def main_teletips():
    async with app:
            while True:
                print("Checking...")
                xxx_teletips = f"📈 | ** Sᴘʟ Nᴇᴛᴡᴏʀᴋ™ Bot Status**"
                alfa = 0
                for bot in BOT_LIST:
                    try:
                        yyy_teletips = await app.send_message(bot, "/start")
                        aaa = yyy_teletips.id
                        await asyncio.sleep(10)
                        zzz_teletips = app.get_chat_history(bot, limit = 1)
                        async for ccc in zzz_teletips:
                            bbb = ccc.id
                        if aaa == bbb:
                            xxx_teletips += f"\n\n🤖  @{bot} 💤 \n        └ **Down** ❌ ➤➤ {PLATFORM[alfa] if PLATFORM[alfa] else None} 💿"
                            for bot_admin_id in BOT_ADMIN_IDS:
                                try:
                                    await app.send_message(int(bot_admin_id), f"🚨 **Beep! Beep!! @{bot} is down** ❌")
                                except Exception:
                                    pass
                            await app.read_chat_history(bot)
                            alfa += 1
                        else:
                            xxx_teletips += f"\n\n🤖  @{bot}\n        └ **Alive** ✅ ➤➤ {PLATFORM[alfa] if PLATFORM[alfa] else None} 💿"
                            await app.read_chat_history(bot)
                            alfa += 1
                    except FloodWait as e:
                        await asyncio.sleep(e.x)            
                time = datetime.datetime.now(pytz.timezone(f"{TIME_ZONE}"))
                last_update = time.strftime(f"%d %b %Y at %I:%M %p")
                xxx_teletips += f"\n\n✔️ Last checked on: {last_update} \n\n<i>♻️ Refreshes automatically by every 10 min</i>"
                await app.edit_message_text(int(CHANNEL_OR_GROUP_ID), MESSAGE_ID, xxx_teletips)
                print(f"Last checked on: {last_update}")                
                await asyncio.sleep(600)
                        
app.run(main_teletips())
