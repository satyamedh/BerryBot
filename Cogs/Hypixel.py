from discord import Embed
import pickle
import discord
from discord.ext import commands, tasks
import asyncpixel
import aiohttp
import Huge_variables.bz_id_stuff as bz_ids


class HypixelCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.hypixel = asyncpixel.Hypixel(pickle.load(open("credentials.pkl", 'rb'))['hypixel'])
        self.currentBazaar = None
        self.currentAh = None
        self.Bazaar_Loop.start()
        self.Auction_loop.start()
        self.bz_id_item = bz_ids.id_name
        self.bz_item_id = bz_ids.name_id
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

        e = Embed(title="Here's some info about this API key",
                  description="**PLEASE NOTE IF THIS ISNT YOUR API KEY DESTROY IT IMMEDIATELY AND INFORM THE OWNER**")
        e.add_field(name="Owner", value=owner_name, inline=False)
        e.add_field(name="Global limit (queries / 2 minutes)", value=str(limit), inline=False)
        e.add_field(name="No. of Queries in the past minute", value=str(queries_in_past_min), inline=False)
        e.add_field(name="Total queries", value=str(total_queries), inline=False)

        await ctx.send(embed=e)

    @commands.command()
    async def bazaar(self, ctx, *, itemId=None):
        final_item_id = ""
        final_item_name = ""
        if itemId is None:
            await ctx.send("Pls send item id or item name")
            return
        if itemId in self.bz_id_item.keys():
            final_item_id = itemId
            final_item_name = self.bz_id_item[itemId]
        elif itemId.lower() in self.bz_item_id.keys():
            final_item_id = self.bz_item_id[itemId.lower()]
            final_item_name = self.bz_id_item[final_item_id]

        item_quick_status = self.currentBazaar[final_item_id].quick_status

        e = Embed(title=final_item_name, description=f"Status of {final_item_name} in the past 30 seconds", color=discord.Color.random())
        e.add_field(name="Buy Price", value=round(item_quick_status.buy_price), inline=True)
        e.add_field(name="Sell Price", value=round(item_quick_status.sell_price), inline=True)
        e.add_field(name="Buy Orders", value=item_quick_status.buy_orders, inline=True)
        e.add_field(name="Sell Orders", value=item_quick_status.sell_orders, inline=True)

        await ctx.send(embed=e)

    @tasks.loop(seconds=30)
    async def Bazaar_Loop(self):
        bz = await self.hypixel.bazaar()
        formattedbz = {}
        for item in bz.bazaar_items:
            # print(item)
            formattedbz[item.product_id] = item

        self.currentBazaar = formattedbz

    @tasks.loop(seconds=30)
    async def Auction_loop(self):
        ah = await self.hypixel.auctions()
        formattedahpages = []
        formattedah = []
        for page in range(ah.total_pages):
            page = await self.hypixel.auctions(page=page)
            formattedahpages.append(page)
        for page in formattedahpages:
            for auction in page.auctions:
                formattedah.append(auction)


        self.currentAh = formattedah

    @commands.command()
    async def auction(self, ctx):
        if self.currentAh is None:
            await ctx.send("Auction house is refreshing. please wait")


def setup(bot):
    bot.add_cog(HypixelCog(bot))
