import discord
from discord.ext import commands

import utils.TextUtil as TextUtil
import utils.MediaUtil as MediaUtil

class Initialize:
    
    def __init__(self, _class):
        self.bot = _class.bot
    
        @_class.music.command(
            name="list"
        )
        async def list(self, ctx=None):
            f = '\n'.join(list(map(lambda f:'• '+f, MediaUtil.get_songs())))
            await ctx.send(f"List of songs:\n```{f}```")
            return
