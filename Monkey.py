import os
import time
from os.path import join, dirname

import discord
from discord.ext import commands as dcmd
from dotenv import load_dotenv

import monkey

discord_time_start = time.perf_counter()

print(f"""
___  ___            _               ______       _   
|  \/  |           | |              | ___ \     | |  
| .  . | ___  _ __ | | _____ _   _  | |_/ / ___ | |_ 
| |\/| |/ _ \| '_ \| |/ / _ \ | | | | ___ \/ _ \| __|
| |  | | (_) | | | |   <  __/ |_| | | |_/ / (_) | |_ 
\_|  |_/\___/|_| |_|_|\_\___|\__, | \____/ \___/ \__|
                              __/ |                  
                             |___/   by bemyrequiem

Running Monkey.py {monkey.version()}   
""")

load_dotenv(join(dirname(__file__), '.env'))

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.typing = False
bot = dcmd.Bot(intents=intents, command_prefix=monkey.config.get_prefix(), help_command=None)

@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord in {round(time.perf_counter() - discord_time_start, 2)}s!")
    monkey.events.__init__(bot)
    monkey.cogs.cmds.__init__(bot)

def main():
    bot.run(monkey.config.get_bot_token())

if __name__ == '__main__':
    main()