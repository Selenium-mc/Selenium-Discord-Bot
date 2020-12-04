import discord
from discord.ext import commands

import utils.TextUtil as TextUtil


class TestCog(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name='test', help="A command used for testing. Developers only.", usage="")
    async def test(self, ctx):
        if not 764121607081426945 in list(map(lambda r:r.id,ctx.message.author.roles)):
            await TextUtil.blink(ctx, "You do not have the `wheel` role. noob. get gud.")
            return
        
        react = await TextUtil.wait_react(ctx, self.bot, ctx.message.author.mention+" Are you sure you want to run the test?", ["✅","❌"], True if "del" in ctx.message.content else False)
        if react == "✅":
            embed=discord.Embed(title="Is it really a test?", color=0x52c832)
            embed.add_field(name="testing testing 123!", value='cool', inline=True)
            await ctx.send(embed=embed)
            await ctx.send('\n'.join([f'{c.name} | usage: {c.usage} | aliases: {", ".join(c.aliases)}' for c in self.bot.commands]))
        else:
            await ctx.send("okay, cancelling")


def setup(bot):
    bot.add_cog(TestCog(bot))