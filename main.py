try:
    import os
    import json
    import discord

    from discord.ext import commands
except ImportError:
    os.system('cls & pip install -r requirements.txt')

with open("config.json") as file:
    config = json.load(file)

    token = config.get("token")
    prefix = config.get("prefix")

bot = commands.Bot(
    command_prefix = prefix,
    self_bot = True,
    intents = discord.Intents.all()
)

bot.remove_command("help")

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    bot.load_extension(f'cogs.{filename[:-3]}')

@bot.event
async def on_ready() -> None:
    os.system('cls; clear && mode 80, 20 & title gui')
    print("\t")

bot.run(token, bot = False)
