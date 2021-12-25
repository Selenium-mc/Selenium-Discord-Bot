import discord
from discord.ext import commands
import requests

import utils.TextUtil as TextUtil

class NotExistCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    
    @commands.command(
        name="notexist",
        aliases=["deepfake","fake"],
        help="Gives you a AI generated photo of a given topic",
        usage="notexist <type (word)>"
    )
    async def notexist(self, ctx, dType: str):
        match = TextUtil.find_closest(dType, ["horse", "cat", "person", "artwork"])

        if match:
            img = requests.get(f"https://this{match}doesnotexist.com/{'image' if match == 'person' else ''}").content

            with open("files/fake/image.jpeg", "wb+") as f:
                f.write(img)
            
            await ctx.send(file=discord.File("files/fake/image.jpeg"))

        else:
            await ctx.send("Unknown option")


def setup(bot):
    bot.add_cog(NotExistCog(bot))
