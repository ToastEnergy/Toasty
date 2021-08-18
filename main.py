import datetime, itertools, discord, os, config
from discord.ext import commands

os.environ["JISHAKU_NO_UNDERSCORE"] = "True"
os.environ["JISHAKU_NO_DM_TRACEBACK"] = "True"
os.environ["JISHAKU_HIDE"] = "True"

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix=commands.when_mentioned_or(config.bot.prefix, f"{config.bot.prefix} "), status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.playing, name="Message me for help!"))
bot.load_extension("jishaku")
bot.remove_command("help")
bot.launchtime = datetime.datetime.now()
bot.colour = lambda : next(config.bot.colour)

@bot.event
async def on_ready():
    print("ready as", bot.user)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f"cogs.{filename[:-3]}")

bot.run(config.bot.token)
