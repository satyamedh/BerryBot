import discord
from discord import Embed
from discord.ext import commands

from Cogs.common import report_error


class ErrorHandlerCog(commands.Cog):
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.CommandNotFound):
            return
        if isinstance(error, discord.ext.commands.MissingPermissions):
            await ctx.send("Ummn you don't have permissions to execute this command. lol.")
            return
        await report_error(ctx, error)


def setup(bot):
    bot.add_cog(ErrorHandlerCog(bot))
