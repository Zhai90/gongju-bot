import discord
import os
import json
import subprocess
from discord.ext import bridge
from dotenv import load_dotenv
from util.log import logger
from time import sleep

load_dotenv()
os.system('clear')
logger.success(f"Starting...")

config = ""
with open("config.json") as f:
    config = json.load(f)

intents = discord.Intents.default()
intents.message_content = True
bot = bridge.Bot(
    command_prefix="$",
    intents=intents,
    activity = discord.Game("with cool people (you)."),
    help_command = None
)

base_cogs = [
    "developer",
    "events",
    "utility"
]

calculator_cogs = [
    "mathematics"
]

for cog in base_cogs:
    bot.load_extension(f"cogs.{cog}")
    logger.log(f"Loaded [underline]cogs/{cog}.py[/underline]")

for cog in calculator_cogs:
    bot.load_extension(f"cogs.calculator.{cog}")
    logger.log(f"Loaded [underline]cogs/calculator/{cog}.py[/underline]")

bot.run(os.getenv('TOKEN'))

# check for connectivity issues every 30 seconds
while True:
    def check_internet_connection():
       try:
          subprocess.check_output(["ping", "-c", "1", "8.8.8.8"])
          return True
       except subprocess.CalledProcessError:
          return False
    if not bool(check_internet_connection()):
       logger.warning("Ping [underline]8.8.8.8[/underline] timed out, there could be a connection issue.")
    sleep(30)
