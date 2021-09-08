# credits - shinchan

from . import *


@bot.on(visa_cmd(pattern="song ?(.*)"))
@bot.on(sudo_cmd(pattern="song ?(.*)", allow_sudo=True))
async def _(event):
    visa_ = event.text[4:]
    if visa_ == "":
        return await eor(event, "Give a song name to search")
    visa = await eor(event, f"Searching song `{visa_}`")
    somg = await event.client.inline_query("Lybot", f"{(deEmojify(visa_))}")
    if somg:
        fak = await somg[0].click(Config.LOGGER_ID)
        if fak:
            await bot.send_file(
                event.chat_id,
                file=fak,
                caption=f"**Song by :** {visa_mention}",
            )
        await visa.delete()
        await fak.delete()
    else:
        await visa.edit("**ERROR 404 :** __NOT FOUND__")


CmdHelp("somgs").add_command(
    "so", "<song name>", "Search the given song and uploads to current chat.", "so into your arms"
).add_info(
    "Fastest Song Module."
).add_warning(
    "✅ Harmless Module."
).add()
