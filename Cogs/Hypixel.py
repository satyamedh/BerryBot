import discord
from discord import Embed
import pickle
from discord.ext import commands, tasks
import asyncio
import asyncpixel
import aiohttp

class HypixelCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.hypixel = asyncpixel.Hypixel(pickle.load(open("credentials.pkl", 'rb'))['hypixel'])
        self.currentBazaar = None
        self.Bazaar_Loop.start()

    @commands.command()
    async def key(self, ctx, key):
        key_data = await self.hypixel.key_data(key)
        owner_uuid = key_data.owner
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://api.mojang.com/user/profiles/{owner_uuid}/names') as response:
                json = await response.json()
                owner_name = json[len(json) - 1]["name"]
        limit = key_data.limit
        queries_in_past_min = key_data.queries_in_past_min
        total_queries = key_data.total_queries

        e = Embed(title="Here's some info about this API key", description="**PLEASE NOTE IF THIS ISNT YOUR API KEY DESTROY IT IMMEDIATELY AND INFORM THE OWNER**")
        e.add_field(name="Owner", value=owner_name, inline=False)
        e.add_field(name="Global limit (queries / 2 minutes)", value=str(limit), inline=False)
        e.add_field(name="No. of Queries in the past minute", value=str(queries_in_past_min), inline=False)
        e.add_field(name="Total queries", value=str(total_queries), inline=False)

        await ctx.send(embed=e)

    @commands.command()
    async def bazaar(self, ctx, itemId=None):
        await ctx.send(self.currentBazaar[itemId].quick_status.buy_price)

    @tasks.loop(minutes=1)
    async def Bazaar_Loop(self):
        bz = await self.hypixel.bazaar()
        formattedbz = {}
        for item in bz.bazaar_items:
            # print(item)
            formattedbz[item.product_id] = item

        self.currentBazaar = formattedbz
        # print(self.currentBazaar)







def setup(bot):
    bot.add_cog(HypixelCog(bot))
