import os
import pickle
import random

import asyncio
import discord
from discord.ext import commands
from num2words import num2words

prefix_list = ['l', '|', 'I']


class ServerMgmtCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_guild=True)
    async def prefix(self, ctx):
        random_number = random.randint(0, 16777215)
        hex_number = str(hex(random_number))
        hex_number = int(hex_number, base=16)
        countr = 0
        embed = discord.Embed(title='List of prefixes', color=hex_number)
        if not os.path.isfile(f'data/servers/{ctx.guild.id}_prefixes.pkl'):
            local_prefix_list = prefix_list
            pickle.dump(local_prefix_list, open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'wb'))
        else:
            local_prefix_list = pickle.load(open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'rb'))
        for lprefix in local_prefix_list:
            embed.add_field(name=':' + num2words(countr) + ':' + f'`{lprefix}`', value='\u200b', inline=False)
            countr += 1
        yeno = True
        if countr == 9:
            embed.add_field(name=':heavy_plus_sign:', value='Add a new prefix(lol no max 10)')
            yeno = False
        else:
            embed.add_field(name=':heavy_plus_sign:', value='Add a new prefix')
        msg = await ctx.send(embed=embed)

        for idn in range(countr):
            if idn == 0:
                await msg.add_reaction('0️⃣')
            if idn == 1:
                await msg.add_reaction('1️⃣')
            if idn == 2:
                await msg.add_reaction('2️⃣')
            if idn == 3:
                await msg.add_reaction('3️⃣')
            if idn == 4:
                await msg.add_reaction('4️⃣')
            if idn == 5:
                await msg.add_reaction('5️⃣')
            if idn == 6:
                await msg.add_reaction('6️⃣')
            if idn == 7:
                await msg.add_reaction('7️⃣')
            if idn == 8:
                await msg.add_reaction('8️⃣')
            if idn == 9:
                await msg.add_reaction('9️⃣')
        if yeno:
            await msg.add_reaction('➕')

        def check(reaction, user) -> bool:
            return user == ctx.author

        def check2(msg1) -> bool:
            return msg1.author == ctx.author

        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            return
        else:
            if reaction.emoji == '➕':
                await ctx.send('aight send me da prefix mate! remeber, if the prefix is a word, add a space after it, '
                               'and put it in a code block. like: `hey ` or `!`, if you do something like: `hey` then you '
                               'will have to do something like `heyhelp` not `hey help` so mind the space. How to put in '
                               'a code block: put a backtick(that one below escape), then your new prefix and then '
                               'another backtick. easy right?')
                try:
                    msg2 = await self.bot.wait_for('message', timeout=60.0, check=check2)
                except asyncio.TimeoutError:
                    return
                else:
                    await ctx.send(f'aight {msg2.content} is added to my prefix list!')
                    local_prefix_list = pickle.load(open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'rb'))
                    local_prefix_list.append(msg2.content[1:-1])
                    pickle.dump(local_prefix_list, open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'wb'))
                    return
            elif reaction.emoji == '0️⃣':
                embed = discord.Embed(title=f'What do wanna do with this prefix? \n {local_prefix_list[0]}',
                                      description=':x: Delete da prefix \n '
                                                  ':tools: to edit it', color=hex_number)
                msg = await ctx.send(embed=embed)
                await msg.add_reaction('❌')
                await msg.add_reaction('🛠️')
                try:
                    reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                except asyncio.TimeoutError:
                    return
                else:
                    if reaction.emoji == '❌':
                        await ctx.send('aight deleting that prefix')
                        local_prefix_list.pop(0)
                        pickle.dump(local_prefix_list, open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'wb'))
                        await ctx.send('deleted')
                    elif reaction.emoji == '🛠️':
                        await ctx.send('wuts the new prefix? '
                                       'remeber, if the prefix is a word, add a space after it, '
                                       'and put it in a code block. like: `hey ` or `!`, if you do something like: `hey` then you '
                                       'will have to do something like `heyhelp` not `hey help` so mind the space. How to put in '
                                       'a code block: put a backtick(that one below escape), then your new prefix and then '
                                       'another backtick. easy right?')
                        try:
                            msg3 = await self.bot.wait_for('message', timeout=60.0, check=check2)
                        except asyncio.TimeoutError:
                            return
                        else:
                            await ctx.send(f'aight {msg3.content} is in my prefix list now!')
                            local_prefix_list = pickle.load(open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'rb'))
                            local_prefix_list[0] = msg3.content[1:-1]
                            pickle.dump(local_prefix_list, open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'wb'))
                            return
            elif reaction.emoji == '1️⃣':
                embed = discord.Embed(title=f'What do wanna do with this prefix? \n {local_prefix_list[1]}',
                                      description=':x: Delete da prefix \n '
                                                  ':tools: to edit it', color=hex_number)
                msg = await ctx.send(embed=embed)
                await msg.add_reaction('❌')
                await msg.add_reaction('🛠️')
                try:
                    reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                except asyncio.TimeoutError:
                    return
                else:
                    if reaction.emoji == '❌':
                        await ctx.send('aight deleting that prefix')
                        local_prefix_list.pop(1)
                        pickle.dump(local_prefix_list, open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'wb'))
                        await ctx.send('deleted')
                    elif reaction.emoji == '🛠️':
                        await ctx.send('wuts the new prefix? '
                                       'remeber, if the prefix is a word, add a space after it, '
                                       'and put it in a code block. like: `hey ` or `!`, if you do something like: `hey` then you '
                                       'will have to do something like `heyhelp` not `hey help` so mind the space. How to put in '
                                       'a code block: put a backtick(that one below escape), then your new prefix and then '
                                       'another backtick. easy right?')
                        try:
                            msg3 = await self.bot.wait_for('message', timeout=60.0, check=check2)
                        except asyncio.TimeoutError:
                            return
                        else:
                            await ctx.send(f'aight {msg3.content} is in my prefix list now!')
                            local_prefix_list = pickle.load(open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'rb'))
                            local_prefix_list[1] = msg3.content[1:-1]
                            pickle.dump(local_prefix_list, open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'wb'))
                            return
            elif reaction.emoji == '2️⃣':
                embed = discord.Embed(title=f'What do wanna do with this prefix? \n {local_prefix_list[2]}',
                                      description=':x: Delete da prefix \n '
                                                  ':tools: to edit it', color=hex_number)
                msg = await ctx.send(embed=embed)
                await msg.add_reaction('❌')
                await msg.add_reaction('🛠️')
                try:
                    reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                except asyncio.TimeoutError:
                    return
                else:
                    if reaction.emoji == '❌':
                        await ctx.send('aight deleting that prefix')
                        local_prefix_list.pop(2)
                        pickle.dump(local_prefix_list, open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'wb'))
                        await ctx.send('deleted')
                    elif reaction.emoji == '🛠️':
                        await ctx.send('wuts the new prefix? '
                                       'remeber, if the prefix is a word, add a space after it, '
                                       'and put it in a code block. like: `hey ` or `!`, if you do something like: `hey` then you '
                                       'will have to do something like `heyhelp` not `hey help` so mind the space. How to put in '
                                       'a code block: put a backtick(that one below escape), then your new prefix and then '
                                       'another backtick. easy right?')
                        try:
                            msg3 = await self.bot.wait_for('message', timeout=60.0, check=check2)
                        except asyncio.TimeoutError:
                            return
                        else:
                            await ctx.send(f'aight {msg3.content} is in my prefix list now!')
                            local_prefix_list = pickle.load(open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'rb'))
                            local_prefix_list[2] = msg3.content[1:-1]
                            pickle.dump(local_prefix_list, open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'wb'))
                            return
            elif reaction.emoji == '3️⃣':
                embed = discord.Embed(title=f'What do wanna do with this prefix? \n {local_prefix_list[3]}',
                                      description=':x: Delete da prefix \n '
                                                  ':tools: to edit it', color=hex_number)
                msg = await ctx.send(embed=embed)
                await msg.add_reaction('❌')
                await msg.add_reaction('🛠️')
                try:
                    reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                except asyncio.TimeoutError:
                    return
                else:
                    if reaction.emoji == '❌':
                        await ctx.send('aight deleting that prefix')
                        local_prefix_list.pop(3)
                        pickle.dump(local_prefix_list, open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'wb'))
                        await ctx.send('deleted')
                    elif reaction.emoji == '🛠️':
                        await ctx.send('wuts the new prefix? '
                                       'remeber, if the prefix is a word, add a space after it, '
                                       'and put it in a code block. like: `hey ` or `!`, if you do something like: `hey` then you '
                                       'will have to do something like `heyhelp` not `hey help` so mind the space. How to put in '
                                       'a code block: put a backtick(that one below escape), then your new prefix and then '
                                       'another backtick. easy right?')
                        try:
                            msg3 = await self.bot.wait_for('message', timeout=60.0, check=check2)
                        except asyncio.TimeoutError:
                            return
                        else:
                            await ctx.send(f'aight {msg3.content} is in my prefix list now!')
                            local_prefix_list = pickle.load(open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'rb'))
                            local_prefix_list[3] = msg3.content[1:-1]
                            pickle.dump(local_prefix_list, open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'wb'))
                            return
            elif reaction.emoji == '4️⃣':
                embed = discord.Embed(title=f'What do wanna do with this prefix? \n {local_prefix_list[4]}',
                                      description=':x: Delete da prefix \n '
                                                  ':tools: to edit it', color=hex_number)
                msg = await ctx.send(embed=embed)
                await msg.add_reaction('❌')
                await msg.add_reaction('🛠️')
                try:
                    reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                except asyncio.TimeoutError:
                    return
                else:
                    if reaction.emoji == '❌':
                        await ctx.send('aight deleting that prefix')
                        local_prefix_list.pop(4)
                        pickle.dump(local_prefix_list, open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'wb'))
                        await ctx.send('deleted')
                    elif reaction.emoji == '🛠️':
                        await ctx.send('wuts the new prefix? '
                                       'remeber, if the prefix is a word, add a space after it, '
                                       'and put it in a code block. like: `hey ` or `!`, if you do something like: `hey` then you '
                                       'will have to do something like `heyhelp` not `hey help` so mind the space. How to put in '
                                       'a code block: put a backtick(that one below escape), then your new prefix and then '
                                       'another backtick. easy right?')
                        try:
                            msg3 = await self.bot.wait_for('message', timeout=60.0, check=check2)
                        except asyncio.TimeoutError:
                            return
                        else:
                            await ctx.send(f'aight {msg3.content} is in my prefix list now!')
                            local_prefix_list = pickle.load(open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'rb'))
                            local_prefix_list[4] = msg3.content[1:-1]
                            pickle.dump(local_prefix_list, open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'wb'))
                            return
            elif reaction.emoji == '5️⃣':
                embed = discord.Embed(title=f'What do wanna do with this prefix? \n {local_prefix_list[5]}',
                                      description=':x: Delete da prefix \n '
                                                  ':tools: to edit it', color=hex_number)
                msg = await ctx.send(embed=embed)
                await msg.add_reaction('❌')
                await msg.add_reaction('🛠️')
                try:
                    reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                except asyncio.TimeoutError:
                    return
                else:
                    if reaction.emoji == '❌':
                        await ctx.send('aight deleting that prefix')
                        local_prefix_list.pop(5)
                        pickle.dump(local_prefix_list, open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'wb'))
                        await ctx.send('deleted')
                    elif reaction.emoji == '🛠️':
                        await ctx.send('wuts the new prefix? '
                                       'remeber, if the prefix is a word, add a space after it, '
                                       'and put it in a code block. like: `hey ` or `!`, if you do something like: `hey` then you '
                                       'will have to do something like `heyhelp` not `hey help` so mind the space. How to put in '
                                       'a code block: put a backtick(that one below escape), then your new prefix and then '
                                       'another backtick. easy right?')
                        try:
                            msg3 = await self.bot.wait_for('message', timeout=60.0, check=check2)
                        except asyncio.TimeoutError:
                            return
                        else:
                            await ctx.send(f'aight {msg3.content} is in my prefix list now!')
                            local_prefix_list = pickle.load(open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'rb'))
                            local_prefix_list[5] = msg3.content[1:-1]
                            pickle.dump(local_prefix_list, open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'wb'))
                            return
            elif reaction.emoji == '6️⃣':
                embed = discord.Embed(title=f'What do wanna do with this prefix? \n {local_prefix_list[6]}',
                                      description=':x: Delete da prefix \n '
                                                  ':tools: to edit it', color=hex_number)
                msg = await ctx.send(embed=embed)
                await msg.add_reaction('❌')
                await msg.add_reaction('🛠️')
                try:
                    reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                except asyncio.TimeoutError:
                    return
                else:
                    if reaction.emoji == '❌':
                        await ctx.send('aight deleting that prefix')
                        local_prefix_list.pop(6)
                        pickle.dump(local_prefix_list, open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'wb'))
                        await ctx.send('deleted')
                    elif reaction.emoji == '🛠️':
                        await ctx.send('wuts the new prefix? '
                                       'remeber, if the prefix is a word, add a space after it, '
                                       'and put it in a code block. like: `hey ` or `!`, if you do something like: `hey` then you '
                                       'will have to do something like `heyhelp` not `hey help` so mind the space. How to put in '
                                       'a code block: put a backtick(that one below escape), then your new prefix and then '
                                       'another backtick. easy right?')
                        try:
                            msg3 = await self.bot.wait_for('message', timeout=60.0, check=check2)
                        except asyncio.TimeoutError:
                            return
                        else:
                            await ctx.send(f'aight {msg3.content} is in my prefix list now!')
                            local_prefix_list = pickle.load(open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'rb'))
                            local_prefix_list[6] = msg3.content[1:-1]
                            pickle.dump(local_prefix_list, open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'wb'))
                            return
            elif reaction.emoji == '7️⃣':
                embed = discord.Embed(title=f'What do wanna do with this prefix? \n {local_prefix_list[7]}',
                                      description=':x: Delete da prefix \n '
                                                  ':tools: to edit it', color=hex_number)
                msg = await ctx.send(embed=embed)
                await msg.add_reaction('❌')
                await msg.add_reaction('🛠️')
                try:
                    reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                except asyncio.TimeoutError:
                    return
                else:
                    if reaction.emoji == '❌':
                        await ctx.send('aight deleting that prefix')
                        local_prefix_list.pop(7)
                        pickle.dump(local_prefix_list, open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'wb'))
                        await ctx.send('deleted')
                    elif reaction.emoji == '🛠️':
                        await ctx.send('wuts the new prefix? '
                                       'remeber, if the prefix is a word, add a space after it, '
                                       'and put it in a code block. like: `hey ` or `!`, if you do something like: `hey` then you '
                                       'will have to do something like `heyhelp` not `hey help` so mind the space. How to put in '
                                       'a code block: put a backtick(that one below escape), then your new prefix and then '
                                       'another backtick. easy right?')
                        try:
                            msg3 = await self.bot.wait_for('message', timeout=60.0, check=check2)
                        except asyncio.TimeoutError:
                            return
                        else:
                            await ctx.send(f'aight {msg3.content} is in my prefix list now!')
                            local_prefix_list = pickle.load(open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'rb'))
                            local_prefix_list[7] = msg3.content[1:-1]
                            pickle.dump(local_prefix_list, open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'wb'))
                            return
            elif reaction.emoji == '8️⃣':
                embed = discord.Embed(title=f'What do wanna do with this prefix? \n {local_prefix_list[8]}',
                                      description=':x: Delete da prefix \n '
                                                  ':tools: to edit it', color=hex_number)
                msg = await ctx.send(embed=embed)
                await msg.add_reaction('❌')
                await msg.add_reaction('🛠️')
                try:
                    reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                except asyncio.TimeoutError:
                    return
                else:
                    if reaction.emoji == '❌':
                        await ctx.send('aight deleting that prefix')
                        local_prefix_list.pop(8)
                        pickle.dump(local_prefix_list, open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'wb'))
                        await ctx.send('deleted')
                    elif reaction.emoji == '🛠️':
                        await ctx.send('wuts the new prefix? '
                                       'remeber, if the prefix is a word, add a space after it, '
                                       'and put it in a code block. like: `hey ` or `!`, if you do something like: `hey` then you '
                                       'will have to do something like `heyhelp` not `hey help` so mind the space. How to put in '
                                       'a code block: put a backtick(that one below escape), then your new prefix and then '
                                       'another backtick. easy right?')
                        try:
                            msg3 = await self.bot.wait_for('message', timeout=60.0, check=check2)
                        except asyncio.TimeoutError:
                            return
                        else:
                            await ctx.send(f'aight {msg3.content} is in my prefix list now!')
                            local_prefix_list = pickle.load(open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'rb'))
                            local_prefix_list[8] = msg3.content[1:-1]
                            pickle.dump(local_prefix_list, open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'wb'))
                            return
            elif reaction.emoji == '️⃣9️⃣':
                embed = discord.Embed(title=f'What do wanna do with this prefix? \n {local_prefix_list[9]}',
                                      description=':x: Delete da prefix \n '
                                                  ':tools: to edit it', color=hex_number)
                msg = await ctx.send(embed=embed)
                await msg.add_reaction('❌')
                await msg.add_reaction('🛠️')
                try:
                    reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                except asyncio.TimeoutError:
                    return
                else:
                    if reaction.emoji == '❌':
                        await ctx.send('aight deleting that prefix')
                        local_prefix_list.pop(9)
                        pickle.dump(local_prefix_list, open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'wb'))
                        await ctx.send('deleted')
                    elif reaction.emoji == '🛠️':
                        await ctx.send('wuts the new prefix? '
                                       'remeber, if the prefix is a word, add a space after it, '
                                       'and put it in a code block. like: `hey ` or `!`, if you do something like: `hey` then you '
                                       'will have to do something like `heyhelp` not `hey help` so mind the space. How to put in '
                                       'a code block: put a backtick(that one below escape), then your new prefix and then '
                                       'another backtick. easy right?')
                        try:
                            msg3 = await self.bot.wait_for('message', timeout=60.0, check=check2)
                        except asyncio.TimeoutError:
                            return
                        else:
                            await ctx.send(f'aight {msg3.content} is in my prefix list now!')
                            local_prefix_list = pickle.load(open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'rb'))
                            local_prefix_list[9] = msg3.content[1:-1]
                            pickle.dump(local_prefix_list, open(f'data/servers/{ctx.guild.id}_prefixes.pkl', 'wb'))
                            return

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        if not ctx.author.top_role.position > member.top_role.position:
            await ctx.send("He has a higher role that you buddy! sorry I cant ban him!")
            return
        fsstr = ""
        for i in reason:
            fsstr = f"{fsstr} {i}"
        reason = fsstr
        try:
            await member.ban(reason=reason)
        except Exception as e:
            await ctx.send(f"Could not ban {member}! \n ERROR: {e}")
            return
        await ctx.send(f"{member} has been banned woo, reason:{reason})    https://www.tenor.com/bfuQS.gif")
        await member.send(f"U were were BANNED FROM {ctx.guild.name} for {reason}, bye bye")

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user: discord.Member, reasonarg=None):
        fsstr = ""
        for i in reasonarg:
            fsstr = f"{fsstr} {i}"
        reason = fsstr
        await user.kick(reason=reason)
        await ctx.send(f"{user.mention} has been kicked woo, reason:{reason})    https://tenor.com/IDX1.gif")
        await user.send(f"U were were KICKED FROM {ctx.guild.name} for {reason}, come back soon :sad:")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def deleteallchannels(self, ctx):
        def check(message) -> bool:
            return ctx.author == message.author

        embed = discord.Embed(title='ARE YOU FREAKING SURE?',
                              description='ARE YOU SURE? THIS WILL DELETE ALL THE CHANNELS, VOICE CHANNELS AND '
                                          'CATEGORIES. THIS ACTION AINT REVERSABLE @everyone')
        await ctx.send(embed=embed)
        try:
            message = await self.bot.wait_for('message', timeout=5.5, check=check)
        except asyncio.TimeoutError:
            await ctx.send('aight, no bombing of channels today')
        else:
            if message.content == 'y':
                await ctx.send('aight, server dead! @everyone IF THIS IS A RAID IMMEDIATELY CONTACT ADMINS')

                channels = ctx.guild.channels
                for i in channels:
                    try:
                        await i.delete()
                    except Exception:
                        pass
            else:
                await ctx.send('aight!')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def banallmembers(self, ctx):
        def check(message) -> bool:
            return ctx.author == message.author

        embed = discord.Embed(title='ARE YOU FREAKING SURE?',
                              description='ARE YOU SURE? THIS WILL BAN EACH AND EVERY PERSON IT CAN. THIS ACTION AINT REVERSABLE @everyone')
        await ctx.send(embed=embed)
        try:
            message = await self.bot.wait_for('message', timeout=5.5, check=check)
        except asyncio.TimeoutError:
            await ctx.send('aight, no bombing of server today')
        else:
            if message.content == 'y':
                await ctx.send('aight, server dead! @everyone IF THIS IS A RAID CONTACT ADMINS IMMEDIATELY')

                channels = ctx.guild.members
                for i in channels:
                    try:
                        await i.ban()
                    except Exception as e:
                        pass
            else:
                await ctx.send('bruh, aight')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def kickallmembers(self, ctx):
        def check(message) -> bool:
            return ctx.author == message.author

        embed = discord.Embed(title='ARE YOU FREAKING SURE?',
                              description='ARE YOU SURE? THIS WILL KICK EACH AND EVERY PERSON IT CAN. THIS ACTION AINT REVERSABLE @everyone')
        await ctx.send(embed=embed)
        try:
            message = await self.bot.wait_for('message', timeout=5.5, check=check)
        except asyncio.TimeoutError:
            await ctx.send('aight, no bombing of server today')
        else:
            if message.content == 'y':
                await ctx.send('aight, server dead! @everyone IF THIS IS A RAID IMMEDIATELY CONTACT STAFF')
                channels = ctx.guild.members
                for i in channels:
                    try:
                        await i.kick()
                    except Exception as e:
                        pass
            else:
                await ctx.send('aight')

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, user, amt: int = 5):
        if isinstance(user, discord.Member):
            def check(m):
                return m.author == user
        elif isinstance(user, str):
            if user == "embeds":
                def check(m):
                    if not m.embeds:
                        return False
                    else:
                        return True
            elif user == "bots":
                def check(m):
                    return m.author.bot

            elif user == "humans":

                def check(m):
                    if m.author.bot:
                        return False
                    else:
                        return True
            elif user.startswith("startswith"):
                the_key = user[9:]

                def check(m):
                    if m.content.startswith(the_key):
                        return True
                    else:
                        return False

            elif user.startswith("endswith"):
                the_key = user[9:]

                def check(m):
                    if m.content.endswith(the_key):
                        return True
                    else:
                        return False
        await ctx.channel.purge(check=check, limit=amt)


def setup(bot):
    bot.add_cog(ServerMgmtCog(bot))