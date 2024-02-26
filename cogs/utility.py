import datetime
import discord
from discord.ext import commands
from util.log import logger
from main import config

class Utility(commands.Cog):
    def __init__(self, bot: discord.Bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx: commands.Context):
        await ctx.reply(f"API Latency: {str(self.bot.ws.latency * 1000)[:6]}ms")

    @commands.command()
    async def help(self, ctx: commands.Context):
        assert self.bot.user is not None
        embed = discord.Embed(
            title = "Help",
            description = f"""
            You can find the list of all the commands by category [here](https://www.google.com/).

            You can ask questions, suggest ideas, and report bugs [here]({config["server_url"]}).
            """,
            color = discord.Color.gold(),
            timestamp = datetime.datetime.today()
        )
        embed.set_author(name = "Gōngjù", icon_url = str(self.bot.user.display_avatar))
        embed.set_footer(text = f'Version: {config["bot_version"]}')

        await ctx.reply(embed = embed)

    @commands.command()
    async def about(self, ctx: commands.Context):
        assert self.bot.user is not None
        embed = discord.Embed(
            title = "About",
            color = discord.Color.gold(),
            timestamp = datetime.datetime.today()
        )
        embed.add_field(name = "WS Latency", value = f"{str(self.bot.ws.latency * 1000)[:6]}ms", inline=True)
        embed.add_field(name = "Total Guilds", value = str(len(self.bot.guilds)), inline=True)
        embed.add_field(name = "Total Commands", value = str(len(self.bot.commands)))
        embed.add_field(name = "Version", value = f'{config["bot_version"]}')
        embed.set_author(name = "Gōngjù", icon_url = str(self.bot.user.display_avatar))
        embed.set_footer(text = "Thank you for using Gōngjù!")

        await ctx.reply(embed = embed)

def setup(bot: discord.Bot):
    bot.add_cog(Utility(bot))
