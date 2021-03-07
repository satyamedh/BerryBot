import pickle
import random
import discord
import asyncio

import requests
from discord.ext import commands

from main import meme_webhooks, meme_ids, meme_image_urrals, meme_post_objects


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

    @commands.command()
    @commands.has_permissions(manage_guild=True)
    async def automeme(self, ctx, channel: discord.TextChannel = None):
        if channel is None:
            await ctx.send('BRUH MENTION A CHANNEL!')
            return
        avaurl = await self.bot.user.avatar_url.read()
        webhook = await channel.create_webhook(name="BerryBot" + ' Automeme', avatar=avaurl)
        url = webhook.url
        meme_webhooks.append(url)
        pickle.dump(meme_webhooks, open('data/meme_urls.pkl', 'wb'))
        await ctx.send('aight b, automeme setup!')

    @commands.command()
    async def meme(self, ctx):
        random_number = random.randint(0, 16777215)
        hex_number = str(hex(random_number))
        ranno = random.randint(0, len(meme_ids))
        slice1 = str(meme_image_urrals[ranno])[2:-1]
        post_obj = meme_post_objects[ranno]
        embed = discord.Embed(title=post_obj.title, color=int(hex_number, base=16))
        try:
            embed.set_image(url=slice1)
        except IndexError:
            return
        embed.set_footer(text=f'\U00002b06 {post_obj.score} | Api by reddit')
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(FunCog(bot))




