import discord
from discord.ext import commands

from fuzzywuzzy import process
import os
import typing
import asyncio
import random


class PortNuberCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="portnuber",
        help="Shows you your port nuber.",
        usage="portnuber"
    )
    async def portnuber(self, ctx):
        embed = discord.Embed(
            title="Port Nuber",
            color=0x2F4186
        )
        embed.add_field(
            name='Port Nuber',
            value='E'
        )
        embed.add_field(
            name='25565 or something it is just the default i think',
            value='What is it though?'
        )
        embed.set_footer(text='Port Nuber Service')

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(PortNuberCog(bot))