import json
import monkey
import discord

def __init__(bot):
    join(bot)
    leave(bot)
    message(bot)

def join(bot):
    @bot.event
    async def on_member_join(member):
        await member.create_dm()
        await member.dm_channel.send(
            f"Hi {member.name}! Thank's for joining the monkeys"
        )

def leave(bot):
    pass

def message(bot):
    @bot.event
    async def on_message(message):
        if message.author == bot.user:
            return
        
        print(
            f"Message from {message.author} in {message.guild} ({message.channel}): {message.content} @ {monkey.time()}"
        )

        if msg := monkey.messages.check_keywords(message.content):
            await message.channel.send(msg)

        await bot.process_commands(message)
        