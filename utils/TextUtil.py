import discord
from discord.ext import commands

import asyncio
from fuzzywuzzy import process

import utils.TextUtil as TextUtil


def find_closest(string, options, margin=75):
    match = process.extractOne(string, [*options])
    print(f'{string} => {options}  {match[0]} ({match[1]}%)')
    return match[0] if match[1] >= margin else False


async def send_loading(channel):
    return await channel.send("<a:discord_loading:779085179657781251>")


def parse_filename(fn):
    return ''.join(c for c in fn if c.isalnum())


async def wait_react(ctx, bot, msg, emojis, delete=False):
    target = await ctx.send(msg)
    for e in emojis: await target.add_reaction(e)

    def check(reaction, user):
        return reaction.message.id == target.id and user == ctx.message.author and str(reaction.emoji) in emojis

    try:
        reaction, user = await bot.wait_for('reaction_add', timeout=10.0, check=check)
    except asyncio.TimeoutError:
        return False
    else:
        if delete: await target.delete()
        return reaction.emoji


async def blink(ctx, blink, wait=3, forcedel=False):
    msg = await ctx.channel.send(blink)
    await asyncio.sleep(wait)

    if forcedel or ctx.channel.id == 737096170043605032:
        await msg.delete()