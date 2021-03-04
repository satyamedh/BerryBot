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
from youtube_search import YoutubeSearch


class UtilCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.datadir = str(pathlib.Path(__file__).parent.absolute()) + "/data"

    @commands.command()
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
            await ctx.send('lol ok, heres the syntax: `hey search [youtube|google, sugggest more using `{prefix}suggesest`] '
                           '<no of results, max 20> (keywords)`')
            return
        if search_keywords is None:
            await ctx.send(f'LOL Tell me search keywords to search for \U0001f923, ' + 'lol ok, heres the syntax: `{prefix}'
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

def setup(bot):
    bot.add_cog(UtilCog(bot))