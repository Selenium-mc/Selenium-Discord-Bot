import discord
from discord.ext import commands
import requests
import json


class SBStatsCog(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="sbstats",
        aliases=["sstat"],
        help="Get stats of somebody in skyblock",
        usage="sbstats <username (String)> <profile name (String)>"
    )
    async def sbstats(self, ctx, playerName):
        resp = requests.get(
            f"https://sky.shiiyu.moe/api/v2/profile/{playerName}"
        )
        print(resp.text)

def setup(bot):
    bot.add_cog(SBStatsCog(bot))
