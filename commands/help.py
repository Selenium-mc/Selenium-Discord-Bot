import discord
from discord.ext import commands

import glob
import os

import utils.TextUtil as TextUtil


class HelpCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.categories = []

        for root, dirs, files in os.walk("commands"):
            for cat in dirs:
                if "_sub" in cat or "__pycache__" in cat:
                    continue

                self.categories.append(cat)


    @commands.command(
        name="help",
        help="Shows a help message",
        usage="help (category, command)"
    )
    async def help(self, ctx, category=None):
        embed = None

        for command in self.bot.commands:
            if command.name == category:
                embed=discord.Embed(title=f"{self.bot.command_prefix}{command.name}", color=0x52c832)
                embed.add_field(
                    name=f"{command.help}",
                    value=f"usage: {command.usage}"
                )
                embed.set_footer(text="* means its a required parameter")
                break

        if not embed:
            if not category:
                embed=discord.Embed(title="Commands List", color=0x52c832)
                for cat in self.categories:
                    embed.add_field(name=cat.title(), value=f"`{self.bot.command_prefix}help {cat}`", inline=True)

            else:
                match = TextUtil.find_closest(category, self.categories, 60)
                
                if not match:
                    await ctx.send(f"Unknown category: `{category}`")
                    return
                
                commands = [cmd for cmd in self.bot.commands if cmd.name in [os.path.basename(f).split('.')[0] for f in glob.glob(f"commands/{match}/*.py")]]

                embed=discord.Embed(title=f"{match.title()} Help", color=0x52c832)
                for com in commands:
                    embed.add_field(name=f"{self.bot.command_prefix}{match} {com.usage}", value=com.help, inline=True)
                embed.set_footer(text="* means its a required parameter")

        if not embed:
            await ctx.send(f"Unknown category or command: `{category}`")
            return

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(HelpCog(bot))