import discord
from discord.ext import commands

import utils.TextUtil as TextUtil


class Initialize:
    
    def __init__(self, _class):
        self.bot = _class.bot
    
        @_class.music.command(
            name="disconnect",
            aliases=["dc", "leave"]
        )
        async def disconnect(self, ctx):
            if (vc:=self._class.get("voice")):
                await vc.disconnect
            else:
                await ctx.send("Already disconnected.")
