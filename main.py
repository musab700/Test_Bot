import json
import random
import discord
from discord.ext import commands

client = commands.Bot(command_prefix='^')

data = {}


@client.event
async def on_ready():
    global data
    with open('data.json') as file:
        data = json.load(file)
    print("{} connected".format(client.user))


@client.command()
async def ping(ctx):
    await ctx.send(f'Ping: {round(client.latency * 1000)}ms')


@client.command()
async def cf(message, arg):
    is_heads = random.randint(0, 1)
    input_heads = arg == 'h'
    if is_heads == input_heads:
        await message.channel.send("You win, it was {}".format('heads' if is_heads else 'tails'))
    else:
        await message.channel.send("Sorry, it was {}".format('heads' if is_heads else 'tails'))


@client.command()
async def register(ctx):
    user = str(ctx.message.author.id)
    if user not in data:
        data[user] = 100
        with open('data.json', 'w') as f:
            json.dump(data, f)
    else:
        ctx.send("You're already registered")


with open('properties.json') as properties:
    token = json.load(properties)

client.run(token['token'])
