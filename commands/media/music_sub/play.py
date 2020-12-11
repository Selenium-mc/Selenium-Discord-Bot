import discord
from discord.ext import commands

import utils.TextUtil as TextUtil
import utils.MediaUtil as MediaUtil


class Initialize:
    
    def __init__(self, _class):
        self.bot = _class.bot
        
        @_class.music.command(
            name="play"
        )
        async def play(self, ctx, *args):
            channel = ctx.author.voice.channel
            song = ' '.join(args)
    
            # fuzzy match
            match = TextUtil.find_closest(song, MediaUtil.get_songs(True))
            if match:
                player = discord.FFmpegPCMAudio(f'files/music/{match}.mp3')
                await ctx.send(f"Playing :notes:  `{match}`")
    
                self._class.set("voice", await channel.connect())
                self._class.get("voice").play(player, after=None)
            else:
                await ctx.send(f"Song `{song}` does not exist.")
                return



    