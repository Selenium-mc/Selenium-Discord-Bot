import discord
from discord.ext import commands

import time

import utils.TextUtil as TextUtil


class MsgQueryCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(
        name="msgquery",
        help="Queries all messages from a given channel.",
        usage="msgquery <*channel (#channel)> <*query (strings)>+"
    )
    async def msgquery(self, ctx, channel: discord.TextChannel, *args):
        args = ' '.join(args)

        start = time.time()
        embed=discord.Embed(color=0xa80000)
        
        loadingmsg = await TextUtil.send_loading(ctx.channel)
        messages = await channel.history(limit=None).flatten()
        length = len(messages)
        counter = 0

        for i in messages:
            if args in i.content:
                embed.add_field(name=f"{i.author.display_name}", value=i.content)
                counter += 1

        await loadingmsg.edit(content=f"\n\nTime: **{time.time()-start} seconds**\nLooked through {length} message{'s' if length else ''}\n Found {counter} occurances of {args}", embed=embed)


def setup(bot):
    bot.add_cog(MsgQueryCog(bot))
