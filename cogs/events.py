import datetime
import discord
from discord.ext import commands
from util.log import logger
from main import config

class Events(commands.Cog):
    def __init__(self, bot: discord.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        logger.success(f'{self.bot.user} ({self.bot.application_id}) has succesfully logged on!')

    @commands.Cog.listener()
    async def on_guild_join(self, guild: discord.Guild):
        assert self.bot.user is not None
        assert guild.owner_id is not None

        owner = await guild.fetch_member(guild.owner_id)
        embed = discord.Embed(
            title = f"Thank you for inviting me to {guild.name}!",
            description = f"""
                Thanks to you, the bot is now in {len(self.bot.guilds)} total servers!

                You can visit our [website](https://www.google.com/) or use `$help` anywhere to get started!

                If something wrong happens, or you manage to think of a very specific command that could be added to the bot, feel free to join our [support server]({config["server_url"]}) as I'd love to hear your thoughts.

                You can find the source code and the changelogs [here]({config["github_url"]}).

                Gōngjù, or 工具 in Mandarin Chinese, literally translates to \"tool\" when translated to English, is an utility-based bot designed for the use and the user. Containing a myriad commands for both niche and every-day use, this bot is going to make things easier, like bots should.

                Made with ❤️, ☕️ and 🍵 by <@360235359746916352>.

                ᴅɪsᴄʟᴀɪᴍᴇʀ: ɴᴏ, ᴛʜɪs ɪs ɴᴏᴛ ᴍᴀᴅᴇ ʙʏ ᴛʜᴇ ᴄʜɪɴᴇsᴇ ᴛᴏ sᴛᴇᴀʟ ʏᴏᴜʀ ɪɴғᴏ. ʏᴇs, ᴛʜᴇ ᴄʀᴇᴀᴛᴏʀ (ᴍᴇ) ɪs ᴄʜɪɴᴇsᴇ. ɴᴏ, ɪ ᴏɴʟʏ ɴᴀᴍᴇᴅ ᴛʜᴇ ʙᴏᴛ ʟɪᴋᴇ ᴛʜɪs ʙᴇᴄᴀᴜsᴇ ɪ ᴅɪᴅɴ'ᴛ ʜᴀᴠᴇ ɢᴏᴏᴅ ɪᴅᴇᴀs, ɴᴏᴛ ʙᴇᴄᴀᴜsᴇ ɪ ᴏɴʟʏ ᴡᴀɴᴛ ᴛʜɪs ᴛᴏ ʙᴇ ᴜsᴇᴅ ʙʏ ᴄʜɪɴᴇsᴇ ᴘᴇᴏᴘʟᴇ, ᴏʀ ᴀɴʏᴛʜɪɴɢ ʟɪᴋᴇ ᴛʜᴀᴛ.
                """,
            color = discord.Colour.gold(),
            timestamp = datetime.datetime.today()
        )
        embed.set_author(name = "Gōngjù Team", icon_url = str(self.bot.user.display_avatar))
        embed.set_footer(text = f'Version: {config["bot_version"]}')
        embed.set_image(url = config["invite_banner"])

        await owner.send(embed = embed)

    async def cog_command_error(self, ctx, error):
        if isinstance(error, discord.HTTPException) or isinstance(error, discord.Forbidden):
            logger.warning(f"Could not find guild owner of {ctx.guild_id}")
        else:
            raise error

def setup(bot):
    bot.add_cog(Events(bot))
