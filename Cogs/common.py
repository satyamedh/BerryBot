import discord
from discord import Embed
from random import randint
import traceback
import os


async def report_error(ctx, e: Exception):
    if not os.path.exists('data'):
        os.makedirs('data')
    if not os.path.exists('data/Exceptions'):
        os.makedirs('data/Exceptions')
    if not os.path.exists(f'data/Exceptions/{e}'):
        os.makedirs(f'data/Exceptions/{e}')
    embed = discord.Embed(
        title='ERRRRROOOOOORR! if you dont a see a "Error reported" message please DM `! ||Satyamedh||#1051` with a screenshot',
        description=f"{e}")
    await ctx.send(embed=embed)
    file = open(f'data/Exceptions/{e}/{randint(0,2147483647)}-Found-Out-By-{ctx.author.id}.txt', 'w')
    traceback.print_exc(file=file)
    file.close()
    e = Embed(title="Error Reported!", description="Error has been reported! thanks for finding this bug!", color=discord.Color.random())
    e.add_field(name="Are you a dev?", value="We'd love it if you will fix it! we'll put your name on the buq squashers list on the readme of the source and will put your name as the footer of this command which caused this error")
    await ctx.send(embed=e)
