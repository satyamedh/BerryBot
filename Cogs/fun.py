import random
import discord
import asyncio
from discord.ext import commands


class FunCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def choose(self, ctx, *, opts=None):
        opts = opts.split(',')
        await ctx.send(f'I Choose:`{random.choice(opts)}`')

    @commands.command()
    async def memkick(self, ctx, member: discord.Member):
        await ctx.send(f'kicked {member.mention}!')
        await member.send(f'{ctx.author.mention} Wanted to kick you lolololol. server:`{ctx.guild.name}`')
        await asyncio.sleep(5)
        await ctx.send(f'jk I didn\'t kick {member.mention}')

    @commands.command()
    async def memban(self, ctx, member: discord.Member):
        await ctx.send(f'BANNED {member.mention}!')
        await member.send(f'{ctx.author.mention} Wanted to ban you lolololol. server:`{ctx.guild.name}`')
        await asyncio.sleep(10)
        await ctx.send(f'jk I didn\'t BAN {member.mention} from existance')







