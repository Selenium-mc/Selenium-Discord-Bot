import discord
from discord.ext import commands
# from discord.utils import get

import random


class EmojisCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(
        name="emojis",
        help="Gets all emojis from the current guild/server.",
        usage="emojis"
    )
    async def emojis(self, ctx):
        emojis = [
            f"<:{e.name}:{e.id}>"
            for e in 
            ctx.message.guild.emojis
        ]
        await ctx.send(' '.join(emojis))
        

def setup(bot):
    bot.add_cog(EmojisCog(bot))
    