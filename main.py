import discord
from discord.ext import commands

import keep_online
import os


keep_online.start()
bot = commands.Bot(command_prefix=';', help_command=None)

exts = []

for root, dirs, files in os.walk("commands", topdown=False):
    for name in files:
        if "_sub" in root or "__pycache__" in root:
            continue
            
        if name.endswith(".py") and not "__init__" in name:
            exts.append(
                os.path.join(root, name).split(".")[0].replace("/", ".")
            )

for root, dirs, files in os.walk("events", topdown=False):
    for name in files:
        if name.endswith(".py") and not "__pycache__" in name:
            exts.append(
                os.path.join(root, name).split(".")[0].replace("/", ".")
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

#just temp code to register slash command
url = "https://discord.com/api/v8/applications/743517399101210725/guilds/737093341493198949/commands"

json = {
    "name": "help",
    "description": "Run this command to see the bot's commands.",
    "options": [
        {
            "name": "Category",
            "description": "The category of command you want to get help for",
            "type": 3,
            "required": False,
            "choices": [
                {
                    "name": "Rules",
                    "value": "Help about rule commands"
                   
                },
                {
                    "name": "Music",
                    "value": "Help about music commands"
                 
                },
                {
                    "name": "Fun",
                    "value": "Help about fun commands"
                   
                },
                {
                    "name": "Message",
                    "value": "Help about message commands"
                }

            ]
        },

    ]
}

# For authorization, you can use either your bot token 
#headers = {
#    "Authorization": "Bot " + os.getenv("TOKEN")
#}



#r = requests.post(url, headers=headers, json=json)
#print(r.content)

bot.run(os.getenv("TOKEN"))