import discord
from discord.ext import commands

import time
import random

import utils.TextUtil as TextUtil


class GetMsgCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(
        name="getmsg",
        help="Gets a random message from a given channel.",
        usage="getmsg <*channel (#channel)>"
    )
    async def getmsg(self, ctx, channel: discord.TextChannel):

        loadingmsg = await TextUtil.send_loading(ctx.channel)
        start = time.time()
    
        messages = await channel.history(limit=None).flatten()
        length = len(messages)
        chosenmsg = random.choice(messages)
    
        embed=discord.Embed(color=0xa80000)
        embed.set_thumbnail(url=chosenmsg.author.avatar_url)
        embed.add_field(name=f"Typed by {chosenmsg.author}", value=f"{chosenmsg.content}\n\n{chosenmsg.jump_url}", inline=False)
        
        await loadingmsg.edit(content=f"||{ctx.message.author.mention}||\n\nTime: **{time.time()-start} seconds**\nChose from {length} message{'s' if length else ''}", embed=embed)


def setup(bot):
    bot.add_cog(GetMsgCog(bot))
