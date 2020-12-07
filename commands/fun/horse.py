import discord
from discord.ext import commands
import requests


class HorseCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        
    

    @commands.command(
        name="horse",
        aliases=("hoh", "hose"),
        help="Gives you a AI generated horse photo",
        usage="horse"
    )
    async def horse(self, ctx):
        with requests.get("https://thishorsedoesnotexist.com/") as r:
            img_data = r.content
        with open('files/horses/horse.jpeg', 'wb') as handler:
            handler.write(img_data)
        
        await ctx.send(file=discord.File("files/horses/horse.jpeg"))


def setup(bot):
    bot.add_cog(HorseCog(bot))