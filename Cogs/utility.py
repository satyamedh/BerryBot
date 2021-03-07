import string
from Cogs.common import *
import discord
import unicodedata
from discord.ext import commands
import random
import asyncio

valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
dc_chards = "`~!@#$%^&*()-_= .,;!?:" + string.ascii_letters + string.digits


class UtilCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['source', 'source-code', 'sourcecode'])
    async def github(self, ctx):
        await ctx.send(
            'I see, you wanna see the source, okay so 1st promise that you will not misuse the source code, you will have to read this licence: http://bit.ly/gnuafferolicence (yes it is a link shortner, dont worry, no ads, it just counts clicks).')
        await asyncio.sleep(5)
        await ctx.send(
            'Send this in this channel to promise you wont misuse: `I HEREBY AGREE THAT I WILL NOT MISUSE THE SOURCE CODE`')

        def check(msg1):
            return msg1.author.id == ctx.author.id

        try:
            msg = await self.bot.wait_for('message', timeout=5.5, check=check)
        except asyncio.TimeoutError:
            await ctx.send('Timeout!')
            return
        else:
            if msg.content == 'I HEREBY AGREE THAT I WILL NOT MISUSE THE SOURCE CODE':
                await ctx.send(
                    'good, here\'s the code: http://bit.ly/BerryBotSourceCode (yes it is a link shortener, don\'t worry, no ads, it just counts clicks).')
                return
            else:
                await ctx.send('you didnt AGREE so no source code for you!')
                return

    @commands.command(aliases=['dc'])
    async def decancer(self, ctx, member: discord.Member = None):
        if member is None:
            await ctx.send('Bruh tell whome to decancer?')
            return
        name = member.display_name
        olmember = member.display_name
        name = str(unicodedata.normalize('NFKD', name).encode('ascii', 'ignore'))
        await member.edit(nick=name)
        name = member.display_name
        name = ''.join(c for c in name if c in valid_chars)
        await member.edit(nick=name[1:-1])
        await ctx.send(f'decancered `{member.display_name}`. previously `{olmember}`')

    @commands.command()
    async def suggest(self, ctx, *suggestionlist):
        fsuggestion = ''
        for suggestion in suggestionlist:
            fsuggestion = fsuggestion + ' ' + suggestion
        lol = random.randint(1, 99999999)
        try:
            os.makedirs(f'data/suggestions/{ctx.author.id}/')
        except OSError:
            pass
        file = open(f'data/suggestions/{ctx.author.id}/{lol}.txt', 'x')
        file.close()
        file = open(f'data/suggestions/{ctx.author.id}/{lol}.txt', 'w')
        file.write(fsuggestion)
        await ctx.send(
            'Thanks for your suggestion! we will try to implement it and if it does keep your dms open from me. also you\'lle have you\'re name in the footer of the suggested command!')

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    @commands.guild_only()
    async def lock(self, ctx):
        await ctx.send(f'locked {ctx.channel.mention}')
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    @commands.guild_only()
    async def unlock(self, ctx):
        await ctx.send(f'unlocked {ctx.channel.mention}')
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)


def setup(bot):
    bot.add_cog(UtilCog(bot))
