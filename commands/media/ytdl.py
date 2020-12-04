import discord
from discord.ext import commands

from pytube import YouTube
import urllib
import asyncio
import os
import subprocess

import utils.TextUtil as TextUtil


class YtdlCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        self.loadingchars = '▁▂▃▄▅▆▇█▇▆▅▄▃▂'
        self.loadingqueue = {}
    

    async def loading(self, loadmsg, id):
        charpos = (self.loadingqueue[id]["pos"]+1)%13

        await loadmsg.edit(content=self.loadingchars[charpos])
        self.loadingqueue[id] = {"pos":(charpos+1)%13, "end":False}

        await asyncio.sleep(0.5)
        await self.loading(loadmsg, id)

    
    @commands.command(
        name='ytdl',
        help="Downloads a video from YouTube",
        usage="ytdl <*url (string)>"
    )
    async def ytdl(self, ctx, url):
        loadingmsg = await TextUtil.send_loading(ctx.channel)

        # l_id = str(len(self.loadingqueue))
        # self.loadingqueue[l_id] = {"pos":0,"end":False}
        # await self.loading(loadingmsg, l_id)

        video = YouTube(url)
        video.streams.filter(progressive=True, file_extension='mp4').first().download('files/videos')

        # self.loadingqueue[l_id]["end"] = True

        await loadingmsg.edit(content=f"||{ctx.message.author.mention}||\nhttps://Selenium-BOT.seleniumdevs.repl.co/video/{urllib.parse.quote_plus(video.title)}.mp4")
        resp = subprocess.check_output(f"curl -F'file=@files/videos/{video.title}.mp4' https://0x0.st")
        await ctx.send(resp)


def setup(bot):
    bot.add_cog(YtdlCog(bot))
