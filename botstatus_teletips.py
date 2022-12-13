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
    session_string = "BQBiMZkAP_e7w6Jz1zoPb-GJ7rdeRBa1VZVNCLDDmxf5ZKU47ZHkcVERRZnO4DT5ZWIbhVitfWxRkqsOMPLw67SsWG3wfntw9S8B89ZakmsSF_dpZkD_gqs9vLHUuK132rSABUJ63D8h7fjIbymFQ9SO2xwbowelTCOtbSTSUbN8dR4DLAyAqOCuQhFPWAsvuA2hcGB6L_LgLfMtPmd86UkumP_OzP-CBX1bWv49A015T3m4m4Pf2a820Oq0Sd5G1KPXSX_vh7M6nbXNcy_LYQ605VsnX3pJEgmrWx8Ixe5XZWEF4oXlqu4LPqHBrE0xksrQBBupw_3-IAjMtG-25j2WI2TxQQAAAAE35sIdAA"
)
TIME_ZONE = "Asia/Kolkata"
BOT_LIST = ["Spl_Levi_Ackerman_Bot", "spl_afk_bot", "spl_sticker_bot", "spl_string_session_bot"]
CHANNEL_OR_GROUP_ID = -1001401571895
MESSAGE_ID = 3
BOT_ADMIN_IDS = [5868832590, 5232837149]
PLATFORM = ["Vps", "Vps", "Vps", "Dhanush"]

async def main_teletips():
    async with app:
            while True:
                print("Checking...")
                time = datetime.datetime.now(pytz.timezone(f"{TIME_ZONE}"))
                last_update = time.strftime(f"%d %b %Y at %I:%M %p")
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
                xxx_teletips += f"\n\n✔️ Last checked on: {last_update} \n\n<i>♻️ Refreshes automatically by every 10 min</i>"
                await app.edit_message_text(int(CHANNEL_OR_GROUP_ID), MESSAGE_ID, xxx_teletips)
                print(f"Last checked on: {last_update}")                
                await asyncio.sleep(600)
                        
app.run(main_teletips())
