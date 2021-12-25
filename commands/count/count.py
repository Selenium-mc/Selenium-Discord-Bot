import discord
from discord.ext import commands

import utils.TextUtil as TextUtil
import utils.JsonUtil as JsonUtil


class CountCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="count",
        aliases=["number"],
        help="Shows the leaderboard in the count channel.",
        usage="count <leaderboard/update>"
    )
    async def count(self, ctx, command, *args):
        if command == "leaderboard": loadingmsg = await TextUtil.send_loading(ctx.channel)

        channel = self.bot.get_channel(776554955418501141)
        messages = await channel.history(limit=None).flatten()
        
        if command == "leaderboard":

            leaderboard = {}
            for m in messages:
                leaderboard[m.author] = leaderboard[m.author] + 1 if m.author in leaderboard else 1

            leaderboard = {k: v for k, v in sorted(leaderboard.items(), key=lambda item: item[1])[::-1]}  # https://stackoverflow.com/a/613218
    
            embed = discord.Embed(title="Counting leaderboard", color=0x64f7b7)
            for l in leaderboard.items():
                embed.add_field(name=l[0], value=f"Counted **{l[1]}** time{'s' if l[1] > 1 else ''}", inline=False)

            await loadingmsg.edit(content="", embed=embed)
        
        elif command == "update":
            number = list(await channel.history(limit=1).flatten())[-1]
            numberint = int(number.content.split(' ')[0])
            data = JsonUtil.get("count")

            data["776554955418501141"] = {
                "value": numberint,
                "uid": number.author.id
            }

            JsonUtil.dump("count", data)

            await ctx.message.add_reaction("\N{THUMBS UP SIGN}")


def setup(bot):
    bot.add_cog(CountCog(bot))