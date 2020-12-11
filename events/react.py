import discord
from discord.ext import commands

import re


class MessageEventCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        # Prevent bot from responding to itself
        if user == self.bot.user: return

        if reaction.message.attachments:

            # feature im working on which make it so small screenshots can automatically be enlarged
            # by alex
            if reaction.emoji.id == 786997794350825522 and reaction.count == 1:
                try:
                    if message.attachments[0]:
                        if '.png' or '.jpg' or '.jpeg' or '.webp' in message.attachments[0].filename:
                            await message.add_reaction("✅")
                            
                            file = await message.attachments[0].to_file()
                            # await message.channel.send(file=file)
                            print(file.filename)
                    
                            with open(f"files/images/misc/{file.filename}", "wb") as f:
                                # f.write(file.fp)
                                await message.attachments[0].save(f)
        
                            image = Image.open(f"files/images/misc/{file.filename}")
                            width, height = image.size

                            image = image.resize((512, 512))
                            image.save(f"files/images/misc/{file.filename}")
                            file = discord.File(f"files/images/misc/{file.filename}")

                            await reaction.message.reply("Image resized to 512x512", file=file)
                except:
                    await reaction.message.reply("Failed to resize.")


def setup(bot):
    bot.add_cog(MessageEventCog(bot))