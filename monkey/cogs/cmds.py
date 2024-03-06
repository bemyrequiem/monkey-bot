import time

import discord
from discord.ext import commands as dcmd

import monkey

def __init__(bot):
    monkey_help(bot)

def monkey_help(bot):
    bot.remove_command('help')

    @bot.command(aliases=['?'])
    async def help(ctx, *cog):
        if not cog:
            print("Monkey Bot description")
        else:
            if len(cog) > 1:
                print(monkey.messages.too_many_arguments())
            else:
                found = False
                for x in bot.cogs:
                    for y in cog:
                        if x == y:
                            print("Cog description")
                            found = True
                if not found:
                    for x in bot.cogs:
                        for c in bot.get_cog(x).get_commands():
                            if c.name.lower() == cog[0].lower():
                                print("Command description")
                                found = True
                    if not found:
                        print("Not found")