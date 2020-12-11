import discord
from discord.ext import commands
from discord.voice_client import VoiceClient

import ffmpeg


exts = (
    "play",
    "list",
    "disconnect"
)


class MusicCog(commands.Cog):
    
    def __init__(self, bot):
        global commands

        self.bot = bot
        self.voice = None

        for command in exts:
            im = __import__(f"commands.media.music_sub.{command}").media.music_sub.__dict__
            im[command].Initialize(self)
    
    def get(self, k):
        return self.__dict__[k]
    
    def set(self, k, v):
        self.__dict__[k] = v

        
    @commands.group(
        name='music',
        invoke_without_subcommand=True
    )
    async def music(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send("You didn't specify a command!")


def setup(bot):
    bot.add_cog(MusicCog(bot))
