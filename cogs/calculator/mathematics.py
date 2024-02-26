import discord
from discord.ext import commands
from util.usage import incorrect_syntax

class Mathematics(commands.Cog):
    def __init__(self, bot: discord.Bot):
        self.bot = bot

    @commands.command()
    async def plus(self, ctx: commands.Context, *args: int):
        if len(args) < 2:
            await incorrect_syntax(self.bot, "plus", "<num1> [num2] [num3...]")
        else:
            arr = []
            count = 0
            for num in args:
                arr.append(num) if type(num) in (int, float) else None
            for val in arr:
                count += val

            await ctx.reply(f"Sum: `{count}`")

def setup(bot: discord.Bot):
    bot.add_cog(Mathematics(bot))
