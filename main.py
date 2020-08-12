import json
import random
import discord
from discord.ext import commands

client = commands.Bot('.')


@client.event
async def on_ready():
    print('Bot is connected')


# checks client ping
@client.command()
async def ping(ctx):
    await ctx.send(f'Ping: {round(client.latency * 1000)}ms')


@client.command()
async def cf(message, arg):
    num = random.randint(0, 1)
    if arg == 'h' or arg == 't':
        if arg == 'h':
            if num == 0:
                await message.channel.send(f"{message.author.mention} It was heads, you win!")
            else:
                await message.channel.send(f"{message.author.mention} It was tails, you lose!")
        elif arg == 't':
            if num == 0:
                await message.channel.send(f"{message.author.mention} It was heads, you lose!")
            else:
                await message.channel.send(f"{message.author.mention} It was tails, you win!")
    elif arg == "help":
        await message.channel.send("Usage: .cf h/t")
    else:
        return

with open("properties.json") as properties:
    data = json.load(properties)

client.run(data['token'])
