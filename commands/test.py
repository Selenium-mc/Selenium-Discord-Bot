import discord
from discord.ext import commands

import glob
import os

import utils.TextUtil as TextUtil
import utils.JsonUtil as JsonUtil


class TestCog(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name='test', help="A command used for testing. Developers only.", usage="")
    async def test(self, ctx, *args):
        if not 764121607081426945 in list(map(lambda r:r.id,ctx.message.author.roles)):
            await TextUtil.blink(ctx, "You do not have the `wheel` role. noob. get gud.")
            return

        channel = self.bot.get_channel(737096170043605032)
        isRulesChannel = ctx.message.channel.id == 737096170043605032
        rules = JsonUtil.get("rules", "rules")
        ids = JsonUtil.get("rules", "ids")

        for topic in rules:
            if topic == "ids": continue

            em = discord.Embed(title=f"{topic.title()} Rules", color=0x52c832)
            for num in rules[topic]:
                em.add_field(
                    name=f"Rule {num}", value=rules[topic][num], inline=True)
            msg = await channel.send(embed=em)

            ids[topic] = msg.id
        
        JsonUtil.dump("rules", {"rules": rules, "ids": ids})

        if not isRulesChannel:
            await ctx.message.add_reaction("\N{THUMBS UP SIGN}")
        else:
            await ctx.message.delete()


def setup(bot):
    bot.add_cog(TestCog(bot))