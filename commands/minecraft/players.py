import discord
from discord.ext import commands

from mcipc.query import Client


class PlayersCog(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="players",
        aliases=["pl"],
        help="Gets a list of players in a given Minecraft server.",
        usage="players <serverip=play.pixelempiresmc.net (string)>"
    )
    async def players(self, ctx, serverip='play.pixelempiresmc.net'):
        with Client(serverip) as client:
            full_stats = client.full_stats
        
        if full_stats.num_players == 0:
            await ctx.send("No one is online!")
        else:
            await ctx.send(f"Player list: {', '.join(query.players)}")


def setup(bot):
    bot.add_cog(PlayersCog(bot))
