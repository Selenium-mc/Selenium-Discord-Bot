import discord
from discord.ext import commands

import asyncio


class WutCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.command(
        name="._.",
        aliases=["wut"],
        help="Shows your confusion.",
        usage="._. <times (int)>"
    )
    async def wut(self, ctx, times: int=3, delete: bool=False):
        if delete: await ctx.message.delete()
    
        sp=("", " ")
        msg = await ctx.send("("+"._.".join(sp)+")")
    
        for _ in range(times-1):
            await asyncio.sleep(1)
            
            sp = (sp[1], sp[0])
            await msg.edit(content="("+"._.".join(sp)+")")


def setup(bot):
    bot.add_cog(WutCog(bot))
