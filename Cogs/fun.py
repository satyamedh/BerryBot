import random

import asyncio
from discord.ext import commands


class FunCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def choose(self, ctx, *, opts=None):
        opts = opts.split(',')
        await ctx.send(f'I Choose:`{random.choice(opts)}`')


