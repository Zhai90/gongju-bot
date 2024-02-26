import discord
from discord.ext import commands
from util.log import logger
from main import config

class Developer(commands.Cog):
    def __init__(self, bot: discord.Bot):
        self.bot = bot

    @commands.command()
    async def shutdown(self, ctx: commands.Context):
        if ctx.author.id == config["owner_id"]:
            await self.bot.close()

def setup(bot: discord.Bot):
    bot.add_cog(Developer(bot))
