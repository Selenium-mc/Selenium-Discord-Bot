import discord
from discord.ext import commands

import utils.TextUtil as TextUtil
import utils.JsonUtil as JsonUtil


class RulesCog(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        self.channel = bot.get_channel(737096170043605032)

    
    @commands.group(
        name='rules'
    )
    async def rules(self, ctx):
        if not 764121607081426945 in list(map(lambda r: r.id, ctx.message.author.roles)):
            await TextUtil.blink(ctx, "You do not have the `wheel` role.", ctx.message)

    @rules.command(name='init')
    async def init(self, ctx, *args):
        isRulesChannel = ctx.message.self.channel.id == 737096170043605032
        rules = JsonUtil.get("rules", "rules")
        ids = JsonUtil.get("rules", "ids")

        if not "new" in args:
            for id in ids.values():
                msg = await self.channel.fetch_message(id)
                await msg.delete()

        for topic in rules:
            if topic == "ids": continue

            em = discord.Embed(title=f"{topic.title()} Rules", color=0x52c832)
            for num in rules[topic]:
                em.add_field(
                    name=f"Rule {num}", value=rules[topic][num], inline=True)
            msg = await self.channel.send(embed=em)

            ids[topic] = msg.id
        
        JsonUtil.dump("rules", {"rules": rules, "ids": ids})

        if not isRulesChannel:
            await ctx.message.add_reaction("\N{THUMBS UP SIGN}")
        else:
            await ctx.message.delete()
    

    @rules.command(name='add')
    async def add(self, ctx, *args):
        isRulesChannel = ctx.message.self.channel.id == 737096170043605032
        rules = JsonUtil.get("rules", "rules")
        ids = JsonUtil.get("rules", "ids")

        # Create category
        if len(args) == 1:
            if args[0] in rules:
                await TextUtil.blink(ctx, "Category already exists")
                return
    
            rules[args[0]] = {}
            em = discord.Embed(
                title=f"{args[0].title()} Rules",
                color=0x52c832
            )
        
            msg = await self.channel.send(embed=em)
            ids[args[0]] = msg.id
            
        # Add rule to category
        elif len(args) > 1:
            if args[0] == "ids" and not args[0] in rules:
                await TextUtil.blink(ctx, f"Category '{args[0]}' does not exist")
                return
        
            rules[args[0]][str(len(rules[args[0]]) + 1)] = ' '.join(args[1:])
        
            if args[0] != "ids" and args[0] in rules:
                em = discord.Embed(
                    title=f"{args[0].title()} Rules",
                    color=0x52c832
                )
        
                for num in rules[args[0]]:
                    em.add_field(
                        name=f"Rule {num}",
                        value=rules[args[0]][num],
                        inline=True
                    )
        
                msg = await self.channel.fetch_message(ids[args[0]])
                await msg.edit(embed=em)
        
            else:
                await TextUtil.blink(ctx, "Non-existent category")
                return
        
        # 0 arguments
        else:
            await TextUtil.blink(ctx, "Not enough arguments")
            return
        
        JsonUtil.dump("rules", {"rules": rules, "ids": ids})
        
        if not isRulesChannel:
            await ctx.message.add_reaction("\N{THUMBS UP SIGN}")
        else:
            await ctx.message.delete()
    

    @rules.command(name='edit')
    async def edit(self, ctx, *args):
        isRulesChannel = ctx.message.self.channel.id == 737096170043605032
        rules = JsonUtil.get("rules", "rules")
        ids = JsonUtil.get("rules", "ids")

        if len(args) > 2:
            rules[args[0]][args[1]] = ' '.join(args[2:])
        else:
            if not isRulesChannel:
                await ctx.send("Not enough arguments")
            return

        if args[0] != "ids" and (match := TextUtil.find_closest(args[0], rules, 50)):
            if args[0] != match:
                react = await TextUtil.wait_react(ctx, self.bot, f"Did you mean: `{match}`?", ["✅","❌"], True)
                if react and react == "✅":
                    args[0] = match

            em = discord.Embed(
                title=f"{args[0].title()} Rules",
                color=0x52c832
            )
            for num in rules[args[0]]:
                if num == args[1]:
                    rules[args[0]][args[1]] = ' '.join(args[2:])
                    em.add_field(
                        name=f"Rule {num}",
                        value=' '.join(args[2:]),
                        inline=True)
                else:
                    em.add_field(
                        name=f"Rule {num}",
                        value=rules[args[0]][num],
                        inline=True)

            msg = await self.channel.fetch_message(ids[args[0]])
            await msg.edit(embed=em)
        else:
            await TextUtil.blink(ctx, "Non-existent category")
            return
        
        JsonUtil.dump("rules", {"rules": rules, "ids": ids})

        if not isRulesChannel:
            await ctx.message.add_reaction("\N{THUMBS UP SIGN}")
        else:
            await ctx.message.delete()
        

    @rules.command(name='del', aliases='delete')
    async def delcmd(self, ctx, *args):
        isRulesChannel = ctx.message.self.channel.id == 737096170043605032
        rules = JsonUtil.get("rules", "rules")
        ids = JsonUtil.get("rules", "ids")

        if args[0] == "ids" and not args[0] in rules:
            await TextUtil.blink(ctx, f"Category '{args[0]}' does not exist")
            return

        if len(args) == 1:
            react = await TextUtil.wait_react(ctx, self.bot, ctx.message.author.mention+" Are you sure you want to delete this category?", ["✅","❌"], True)
            if react == "✅":
                JsonUtil.rules_backup(JsonUtil.get("rules"), ctx.message.author.id)
    
                rules.pop(args[0])
    
                msg = await self.channel.fetch_message(ids[args[0]])
                await msg.delete()
    
                ids.pop(args[0])
                JsonUtil.dump("rules", {"rules": rules, "ids": ids})

        elif len(args) == 2:
            react = await TextUtil.wait_react(ctx, self.bot, ctx.message.author.mention+" Are you sure you want to delete this rule?", ["✅","❌"], True)
            if react == "✅":
                JsonUtil.rules_backup(JsonUtil.get("rules"), ctx.message.author.id)

                em = discord.Embed(
                    title=f"{args[0].title()} Rules", color=0x52c832)
    
                rules[args[0]].pop(args[1])
                rules[args[0]] = {
                    str(i + 1): list(rules[args[0]].values())[i]
                    for i in range(len(rules[args[0]]))
                }
    
                for num in rules[args[0]]:
                    em.add_field(
                        name=f"Rule {num}", value=rules[args[0]][num], inline=True)
                
                JsonUtil.dump("rules", {"rules": rules, "ids": ids})
    
                msg = await self.channel.fetch_message(ids[args[0]])
                await msg.edit(embed=em)

        else:
            await TextUtil.blink(ctx, "Not enough arguments")
        
        if not ctx.message.self.channel.id == 737096170043605032:
            await ctx.message.add_reaction("\N{THUMBS UP SIGN}")
        else:
            await ctx.message.delete()


    @rules.command(name='json')
    async def json(self, ctx):
        await TextUtil.blink(ctx, "https://repl.it/@SeleniumDevs/Selenium-Bot#data/rules.json")
    

    @rules.command(name='backup')
    async def backup(self, ctx):
        JsonUtil.rules_backup(JsonUtil.get("rules"), ctx.message.author.id)

        if not ctx.message.self.channel.id == 737096170043605032:
            await ctx.message.add_reaction("\N{THUMBS UP SIGN}")
        else:
            await ctx.message.delete()


def setup(bot):
    bot.add_cog(RulesCog(bot))
