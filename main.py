import discord
from discord.ext import commands

import keep_online
import os


keep_online.start()
bot = commands.Bot(command_prefix=';', help_command=None)

exts = (
    "commands.help",
        
    "commands.rules.rules",
    # "commands.rules.init",
    # "commands.rules.add",
    
    "commands.media.ytdl",
    "commands.media.music",
    
    "commands.fun.cat",
    "commands.fun.deletethis",
    "commands.fun.lev",
    "commands.fun.portnuber",
    "commands.fun.wut",
    "commands.fun.horse",
     
    "commands.message.getmsg",
    "commands.message.msgquery",
    "commands.message.emojis",
    
    "commands.minecraft.players",
     
    "commands.count.count",
    
    "events.ready",
    "events.message",
    "events.react",
    
    "commands.test"
)


@bot.command(name="shutdown")
async def shutdown(ctx):
    if not 764121607081426945 in list(map(lambda r:r.id,ctx.message.author.roles)):
        await ctx.send("You do not have the `wheel` role.")
        return
    
    await ctx.send("beep boop... Shutting down")
    try:
        await bot.logout()
    except:
        print("EnvironmentError")
        bot.clear()


@bot.command(name="credits", aliases = ("devs", "contributers"))
async def credits(ctx):
    embed=discord.Embed(title="Developers and Contributers!", color=0x52c832)
    embed.add_field(name="Supercolbat#2697", value="0b0t ~~legend~~ new-midplayer")
    embed.add_field(name="Alex", value="cat")
    embed.add_field(name="Eli", value="am frog **e**")
    await ctx.send(embed=embed)


if __name__ == '__main__':
    for extension in exts:
        bot.load_extension(extension)

bot.run(os.getenv("TOKEN"))