import discord
from discord.ext import commands
from discord.voice_client import VoiceClient

import ffmpeg


class MusicCog(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(
        name='music'
    )
    async def music(self, ctx, command, *args):
        # channel = self.bot.get_channel(737093341493198953)
    
        if command == "play":
            channel = ctx.author.voice.channel
            song = ' '.join(args)
    
            # fuzzy match
            match = TextUtil.find_closest(song, get_songs(True))
            if match:
                player = discord.FFmpegPCMAudio(f'files/music/{match}.mp3')
                await ctx.send(f"Playing :notes:  `{match}`")
                self.voice = await channel.connect()
            else:
                await ctx.send(f"Song `{song}` does not exist.")
                return

        elif command == "list":
            f = '\n'.join(list(map(lambda f:'• '+f, get_songs())))
            await ctx.send(f"List of songs:\n```{f}```")
            return

        elif command in ["disconnect", "dc", "leave"]:
            if self.voice:
                await self.voice.disconnect()
            else:
                await ctx.send("Already disconnected.")

            return
        
        elif command == "state":
            await ctx.send(self.voice)
            return
    
        # https://stackoverflow.com/a/62107725 owo
    
        self.voice.play(player, after=None)


def setup(bot):
    bot.add_cog(MusicCog(bot))
