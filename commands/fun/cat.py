import discord
from discord.ext import commands

import os
import random


class CatCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.lastcat = None
    

    @commands.command(
        name="cat",
        aliases=["george"],
        help="Gets a random cat picture.",
        usage="cat"
    )
    async def cat(self, ctx):
        files = os.listdir("files/images/cats")

        while (f:=random.choice(files)) != self.lastcat:
            self.lastcat = f
            catPicture = discord.File(f"files/images/cats/{f}")
            
            await ctx.send(file=catPicture)
            break


def setup(bot):
    bot.add_cog(CatCog(bot))
