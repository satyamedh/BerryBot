import pickle
import random
import discord
import asyncio

import requests
from discord.ext import commands
import datetime
import humanize

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

        
        
        
    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def gstart(self,ctx,timing,winners,*,prize):
      if timing.endswith('s'):
        seconds = timing[:-1]
        end_delta = datetime.timedelta(seconds = int(seconds))
      if timing.endswith('m'):
        minutes = timing[:-1]
        end_delta = datetime.timedelta(minutes = int(minutes))
      elif timing.endswith('h'):
        hours = timing[:-1]
        end_delta = datetime.timedelta(hours = int(hours))
      start = datetime.datetime.now()
      start_ending_in = start + end_delta
      start_humanize_ending_in = humanize.naturaltime(start_ending_in)
      embed = discord.Embed(title = prize, color = discord.Color.from_rgb(0,255,255))
      embed.description = f"React with 🎉 to enter! \nEnding time: {start_humanize_ending_in} \nHosted by: {ctx.author.mention}"
      embed.timestamp = start_ending_in
      embed.set_footer(text = "Giveaway ending:")
      msg = await ctx.send(embed = embed)
      msgid = msg.id
      await msg.add_reaction("🎉")
      while start_ending_in > datetime.datetime.now():
        await asyncio.sleep(10)
        time_left = (start_ending_in - datetime.datetime.now()).total_seconds()
        time_left_humanize = humanize.precisedelta(time_left)
        embed = discord.Embed(color = discord.Color.from_rgb(0,255,255))
        embed.set_author(name = prize)
        embed.description = f"React with 🎉 to enter! \nEnding time: {time_left_humanize} \nHosted by: {ctx.author.mention}"
        embed.timestamp = start_ending_in
        embed.set_footer(text = "Giveaway ending:")
        await msg.edit(embed = embed)
      gw_msg = await ctx.channel.fetch_message(msgid)
      reactions = gw_msg.reactions
      reaction = reactions[0]
      raffle = await reaction.users().flatten()
      raffle.pop(raffle.index(client.user))
      winner = random.choice(raffle)
      await ctx.send(f"Congratulations {winner.mention}!, you won **{prize}**!")


    @commands.command()
    async def greroll(self,ctx):
      async for message in ctx.channel.history(limit = 50):
        if message.author == client.user:
          if message.embeds:
            if message.embeds[0].description.startswith('React with'):
              gw_msg = message
            else:
              continue
          else:
            continue
        else:
          continue
      reactions = gw_msg.reactions
      reaction = reactions[0]
      raffle = await reaction.users().flatten()
      raffle.pop(raffle.index(client.user))
      winner = random.choice(raffle)
      await ctx.send(f"The new winner is {winner.mention}!, Congratulations!")

     
    
    
    
def setup(bot):
    bot.add_cog(FunCog(bot))




