import random
import discord
import asyncio

import requests
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
        await ctx.send(f'jk I didn\'t BAN {member.mention}')

    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
        responses = ["It is certain.",
                     "It is decidedly so.",
                     "Without a doubt.",
                     "Yes - definitely.",
                     "You may rely on it.",
                     "As I see it, yes.",
                     "Most likely.",
                     "Affirmative.",
                     "Yeah.",
                     "I'm sure.",
                     "Reply hazy, try again.",
                     "Ask again later.",
                     "Better not tell you now.",
                     "Cannot predict now.",
                     "Concentrate and ask again.",
                     "Don't count on it.",
                     "My reply is no.",
                     "My sources say no.",
                     "Umm...No.",
                     "Very doubtful."]
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

    @commands.command()
    async def joke(self, ctx):
        r = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'text/plain'})
        await ctx.send(r.text)






