import os
import string

import discord
import unicodedata
from bs4 import BeautifulSoup
from discord import Embed
# import sqlite3
from discord.ext import commands
import pathlib
# import os
import favicon
from googlesearch import search as gsearch
import random
import mechanize
import requests
from ytpy import YoutubeClient
import asyncio
import aiohttp



valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
dc_chards = "`~!@#$%^&*()-_= .,;!?:" + string.ascii_letters + string.digits


class UtilCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.datadir = str(pathlib.Path(__file__).parent.absolute()) + "/data"

    # @commands.command()
    async def search(self, ctx, platform=None, results_no: int = None, *, search_keywords=None):
        if platform is None:
            await ctx.send(
                'LOL Tell me a platform to search for. currently: `youtube` and `google`, ' + 'lol ok, heres '
                                                                                              'the syntax: '
                                                                                              '`{prefix}search ['
                                                                                              'youtube|google] '
                                                                                              '<no of results, '
                                                                                              'max 20> ('
                                                                                              'keywords)`')
            return

        if results_no is None:
            await ctx.send(
                'lol ok, heres the syntax: `hey search [youtube|google, sugggest more using `{prefix}suggesest`] '
                '<no of results, max 20> (keywords)`')
            return
        if search_keywords is None:
            await ctx.send(
                f'LOL Tell me search keywords to search for \U0001f923, ' + 'lol ok, heres the syntax: `{prefix}'
                                                                            'search [youtube|google] <no of '
                                                                            'results, max 20> (keywords)`')
            return
        if platform == 'youtube':
            fstr = ''
            for str1 in search_keywords:
                fstr = fstr + ' ' + str1
            session = aiohttp.ClientSession()

            client = YoutubeClient(session)

            response = await client.search(fstr)
            print(response)

            await session.close()
            for results1 in results:
                random_number = random.randint(0, 16777215)
                hex_number = int(str(hex(random_number)), base=16)
                embed = Embed(title=results1.get('title'),
                              description=results1.get('channel') + f'\n Duration: ' + str(
                                  results1.get('duration')),
                              color=hex_number)
                embed.set_image(url=results1.get('thumbnails')[0])
                embed.set_footer(
                    text=f'\U0001f440 ' + str(results1.get('views')) + ' URL: http://www.youtube.com' + results1.get(
                        'url_suffix'))
                await ctx.send(embed=embed)

        elif platform == 'google':
            await ctx.send('takes time! have patience! web scraping aint easy!')
            fstr = ''
            for str1 in search_keywords:
                fstr = fstr + ' ' + str1
            for j in gsearch(fstr, tld="co.in", num=10, stop=10, pause=2):
                br = mechanize.Browser()
                # noinspection PyBroadException
                try:
                    br.open(j)
                except Exception:
                    await ctx.send(f'Here\'s the url: {j} This site disallows web scraping.')
                    return

                title = br.title()
                resp = requests.get(j)
                soup = BeautifulSoup(resp.text)
                metas = soup.find_all('meta')
                desc = [meta.attrs['content'] for meta in metas if
                        'name' in meta.attrs and meta.attrs['name'] == 'description']
                try:
                    desc[0]
                except IndexError:
                    desc = [f'Unable to decode description, so you have this as desc lelel. anyway url: {j}']
                embed = Embed(title=title, description=str(desc[0]))
                try:
                    embed.set_image(url=favicon.get(j)[0].url)
                    embed.set_thumbnail(url=favicon.get(j)[1].url)
                except IndexError:
                    embed.set_image(
                        url='https://res.cloudinary.com/dste7lzp4/image/upload/v1599930162/Untitled_dkde04.png')
                    embed.set_thumbnail(
                        url='https://res.cloudinary.com/dste7lzp4/image/upload/v1599930162/Untitled_dkde04.png')
                await ctx.send(embed=embed)

    @commands.command(aliases=['source', 'source-code', 'sourcecode'])
    async def github(self, ctx):
        await ctx.send(
            'I see, you wanna see the source, okay so 1st promise that you will not misuse the source code, you will have to read this licence: http://bit.ly/gnuafferolicence (yes it is a link shortner, dont worry, no ads, it just counts clicks).')
        await asyncio.sleep(5)
        await ctx.send(
            'Send this in this channel to promise you wont misuse: `I HEREBY AGREE THAT I WILL NOT MISUSE THE SOURCE CODE, AND WILL NOT SELF-HOST THE BOT EVEN IF I UNDERSTAND HOW IT WORKS`')

        def check(msg):
            return msg.author.id == ctx.author.id

        try:
            msg = await self.bot.wait_for('message', timeout=5.5, check=check)
        except asyncio.TimeoutError:
            await ctx.send('Timeout!')
            return
        else:
            if msg.content == 'I HEREBY AGREE THAT I WILL NOT MISUSE THE SOURCE CODE, AND WILL NOT SELF-HOST THE BOT EVEN IF I UNDERSTAND HOW IT WORKS':
                await ctx.send(
                    'good boye, heres the code: http://bit.ly/BerryBotSourceCode (yes it is a link shortner, dont worry, no ads, it just counts clicks).')
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
        diplayname = ctx.author.display_name
        diplayname = ''.join(c for c in diplayname if c in valid_chars)
        lol = random.randint(1, 99999999)
        try:
            os.makedirs(f'data/suggestions/{diplayname}/')
        except Exception:
            pass
        file = open(f'data/suggestions/{diplayname}/{lol}.txt', 'x')
        file.close()
        file = open(f'data/suggestions/{diplayname}/{lol}.txt', 'w')
        file.write(fsuggestion)
        await ctx.send('Thanks for your suggestion! we will try to implement it and if it does keey your dms open from me. also you\'lle have you\'re name in the footer of the suggested command!')


def setup(bot):
    bot.add_cog(UtilCog(bot))
