# credit goes to @D3_krish and @official_sameer

from telethon import events
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User
from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot

from . import *


#-------------------------------------------------------------------------------
DEFAULTER = Config.YOUR_NAME

@bot.on(visa_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def up(visa):
    if visa.fwd_from:
        return
    await visa.get_chat()
    await visa.delete()
    await bot.send_file(visa.chat_id, VISA_PIC, caption=VISA_CAPTION)
    await visa.delete()

VISA_PIC = Config.ALIVE_PIC or "https://telegra.ph/file/37ac22fe95355d62c2d76.mp4"
VISA_CAPTION = "🔥 ʟɛɢɛռɖǟʀʏ ǟʄ ʋɨֆǟ-Ӽ ɮօȶ 🔥\n\n"
VISA_CAPTION += (
    f"                __↼𝙼𝙰𝚂𝚃𝙴𝚁⇀__\n  **『 {visa_mention} 』**\n\n"
)
VISA_CAPTION += f"╔═══════════════╗\n"
VISA_CAPTION += f"╠•➳➠ `𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽:` `{tel_ver}` \n"
VISA_CAPTION += f"╠•➳➠ `𝚅𝙴𝚁𝚂𝙸𝙾𝙽:` `{visa_ver}`\n"
VISA_CAPTION += f"╠•➳➠ `𝙶𝚁𝙾𝚄𝙿:`  [𝙹𝙾𝙸𝙽](t.me/Visa_SUPPORT)\n"
VISA_CAPTION += f"╠•➳➠ `𝙲𝙷𝙰𝙽𝙽𝙴𝙻:` [𝙹𝙾𝙸𝙽](t.me/Visa_Update)\n"
VISA_CAPTION += f"╠•➳➠ `𝙲𝚁𝙴𝙰𝚃𝙾𝚁:` [⚡𝙿𝚁𝙾⚡](https://t.me/CALL_ME_VP)\n"
VISA_CAPTION += f"╚═══════════════╝\n\n"
VISA_CAPTION += " [✨𝚁𝙴𝙿𝙾✨](https://github.com/callmevp/VisaXBot) 🔹 [📜𝙻𝙸𝙲𝙴𝙽𝚂𝙴📜](https://github.com/callmevp/VisaXBot/blob/main/LICENSE)"
                            
#_______



@bot.on(visa_cmd(outgoing=True, pattern="awake$"))
@bot.on(sudo_cmd(pattern="awake$", allow_sudo=True))
async def up(visa):
    if visa.fwd_from:
        return
    await visa.get_chat()
    await visa.delete()
    await bot.send_file(visa.chat_id, VISA_PIC, caption=visa_caption)
    await visa.delete()

visa_caption = f"🔥 ʟɛɢɛռɖǟʀʏ ǟʄ ʋɨֆǟ-Ӽ ɮօȶ 🔥\n\n"
visa_caption += f"≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈\n\n"
visa_caption += f"**{Config.ALIVE_MSG}**\n\n"
visa_caption += f"≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈\n\n"                
visa_caption += f"𖣘 𝙰𝙱𝙾𝚄𝚃 𝙼𝚈 𝚂𝚈𝚂𝚃𝙴𝙼 𖣘\n\n"
visa_caption += f"➾ `𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽` ➣ `{tel_ver}` \n"
visa_caption += f"➾ `𝚂𝚄𝙳𝙾 𝙼𝙾𝙳𝙴:` ➣ `{is_sudo}`\n"
visa_caption += f"➾ 𝙼𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻: ➣ [𝙹𝙾𝙸𝙽](t.me/Config.YOUR_CHANNEL)\n"
visa_caption += f"➾ 𝙼𝚈 𝙶𝚁𝙾𝚄𝙿: ➣ [𝙹𝙾𝙸𝙽](t.me/Config.YOUR_GROUP)\n\n"
visa_caption += f"[✨ 𝐃𝐄𝐏𝐋𝐎𝐘 𝐘𝐎𝐔𝐑 𝐕𝐈𝐒𝐀-𝐗 𝐁𝐎𝐓 ✨](https://github.com/callmevp/VisaXBot)\n" 
                                     
                                 
                
CmdHelp("alive").add_command(
  "alive", None, "Shows the Default Alive Message"
).add_command(
  "Awake", None, "Shows Inline Alive Menu with more details."
).add_warning(
  "✅ Harmless Module"
).add()
