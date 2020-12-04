import discord
from discord.ext import commands

from fuzzywuzzy import process


class FunCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(
        name="lev",
        help="Uses Levenshtein distance to find the most similar word in a list.",
        usage="lev <*sample (string)> <*words (strings)>+"
    )
    async def lev(self, ctx, st, *ops):
        match = process.extractOne(st, ops)
        await ctx.send(f"{st} is {match[1]}% similar to {match[0]}")


def setup(bot):
    bot.add_cog(FunCog(bot))
