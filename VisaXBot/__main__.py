import glob
import os
import sys
from pathlib import Path

import telethon.utils
from telethon import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest

from VisaXBot import LOGS, bot, tbot
from VisaXBot.config import Config
from VisaXBot.utils import load_module
from VisaXBot.version import __visa__ as visaver
hl = Config.HANDLER
VISA_PIC = Config.ALIVE_PIC or "https://telegra.ph/file/ea9e11f7c9db21c1b8d5e.mp4"

# let's get the bot ready
async def visa_bot(bot_token):
    try:
        await bot.start(bot_token)
        bot.me = await bot.get_me()
        bot.uid = telethon.utils.get_peer_id(bot.me)
    except Exception as e:
        LOGS.error(f"VISAX_SESSION - {str(e)}")
        sys.exit()


# VisaXBot starter...
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    try:
        if Config.BOT_USERNAME is not None:
            LOGS.info("Checking Telegram Bot Username...")
            bot.tgbot = TelegramClient(
                "BOT_TOKEN", api_id=Config.APP_ID, api_hash=Config.API_HASH
            ).start(bot_token=Config.BOT_TOKEN)
            LOGS.info("Checking Completed. Proceeding to next step...")
            LOGS.info("🔰 VISA-X BOT KO START KR RHE HAI BOSS 🔰")
            bot.loop.run_until_complete(visa_bot(Config.BOT_USERNAME))
            LOGS.info("🔥 VISA-X BOT STARTUP COMPLETE 🔥")
        else:
            bot.start()
    except Exception as e:
        LOGS.error(f"BOT_TOKEN - {str(e)}")
        sys.exit()

# imports plugins...
path = "VisaXBot/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))

# Extra Modules...
# extra_repo = Config.EXTRA_REPO or "https://github.com/The-VisaXBot/Extra"
# if Config.EXTRA == "True":
#     try:
#         os.system(f"git clone {extra_repo}")
#     except BaseException:
#         pass
#     LOGS.info("Installing Extra Plugins")
#     path = "VisaXBot/plugins/*.py"
#     files = glob.glob(path)
#     for name in files:
#         with open(name) as ex:
#             path2 = Path(ex.name)
#             shortname = path2.stem
#             load_module(shortname.replace(".py", ""))


# let the party begin...
LOGS.info("Starting Bot Mode !")
tbot.start()
LOGS.info("⚡ YOUR BOT IS NOW READY BABE ⚡")
LOGS.info(
    "CONGRATULATIONS 🥳🥳🎊🎊 YOUR 𝘃ɪ𝒔ѧ-X ʙο𝞽 IS DEPLOYED 🎊 ... NOW TYPE .ping OR .alive TO CHECK OUR AMAZING BOT 🥳🔥 IF U HAVE ANY PROBLEM THEN JOIN @Visa_Update"
)

# that's life...
async def visa_is_on():
    try:
        if Config.LOGGER_ID != 0:
            await bot.send_file(
                Config.LOGGER_ID,
                VISA_PIC,
                caption=f"#START \n\nDeployed ʋɨֆǟ-Ӽ ɮօȶ Successfully\n\n**ʋɨֆǟ-Ӽ ɮօȶ - {visaver}**\n\nType `{hl}ping` or `{hl}alive` to check! \n\nJoin [νιѕα-χ вσт ¢нαηηєℓ](t.me/Visa_Update) for Updates & [νιѕα-χ вσт ѕυρρσят](t.me/Visa_support) for any query regarding ʋɨֆǟ-Ӽ ɮօȶ",
            )
    except Exception as e:
        LOGS.info(str(e))

# Join VisaXBot Channel after deploying 🤐😅
    try:
         await bot(JoinChannelRequest("@Visa_Update"))
         await bot(JoinChannelRequest("@Visa_SUPPORT"))
         await bot(JoinChannelRequest("@b_e_s_t_s_t_a_t_u_s"))
    except BaseException:
        pass

# Why not come here and chat??
#    try:
#        await bot(JoinChannelRequest("@WeGetTogether"))
#    except BaseException:
#        pass


bot.loop.create_task(visa_is_on())

if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    bot.run_until_disconnected()

# VisaXBot
