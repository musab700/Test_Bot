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
        embed_win = discord.Embed(title="",
                                  description="**You win!** It was {}".format('heads' if is_heads else 'tails'),
                                  color=0xff3d00)
        await message.channel.send(embed=embed_win)
    else:
        embed_lose = discord.Embed(title="",
                                   description="**You lose!**, It was {}".format('heads' if is_heads else 'tails'),
                                   color=0xff3d00)
        await message.channel.send(embed=embed_lose)


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
