import discord
from discord.ext import commands


class DeleteThisCog(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="deletethis",
        help="Deletes your message in a given time.",
        usage="deletethis <time=1 (int)>"
    )
    async def deletethis(self, ctx, time=1):
        await ctx.message.delete(delay=time)


def setup(bot):
    bot.add_cog(DeleteThisCog(bot))
