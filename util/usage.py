from discord import Embed, Color, Bot
from main import config

class Syntax():
    async def incorrect_syntax(self, bot: Bot, command: str, syntax: str) -> Embed:
        assert bot.user is not None
        embed = Embed(
            title = "Invalid syntax!",
            description = f"""
            Correct Usage:
            ```
            ${command} {syntax}```
            """,
            color = Color.red()
        )
        embed.set_author(name = "Gōngjù", icon_url = str(bot.user.display_avatar))
        embed.set_footer(text = f'Version: {config["bot_version"]}')

        return embed

incorrect_syntax = Syntax().incorrect_syntax
