import discord
from discord.ext import commands
import requests

import utils.TextUtil as TextUtil

class NotExistCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    
    @commands.command(
        name="notexist",
        aliases=["deepfake"],
        help="Gives you a AI generated photo of a given topic",
        usage="notexist <type (word)>"
    )
    async def notexist(self, ctx, dType: str):
        match = TextUtil.closest(dType, ["horse", "cat", "person"])

        if match:
            img = requests.get(f"https://this{match}doesnotexist.com/").content

            with open("files/fake/image.jpeg", "wb") as f:
                f.write(img_data)
            
            await ctx.send(file=discord.File("files/horses/horse.jpeg"))

        else:
            await ctx.send("Unknown option")


def setup(bot):
    bot.add_cog(NotExistCog(bot))
