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
async def coinf(ctx, arg):
    h_or_t = random.randint(0, 1)
    coinflip_embed = discord.Embed
    if arg == 'h':
        if h_or_t == 0:
            coinflip_embed.title = "You win it was heads"
            await ctx.send(embed=coinflip_embed)
        else:
            coinflip_embed.title = "You lose it was tails"
            await ctx.send(embed=coinflip_embed)
    elif arg == 't':
        if h_or_t == 1:
            coinflip_embed.title = "You win, it was tails"
            await ctx.send(embed=coinflip_embed)
        else:
            coinflip_embed.title = "You lose, it was heads"
            await ctx.send(embed=coinflip_embed)
    else:
        coinflip_embed.title = "Invalid usage"
        await ctx.send(embed=coinflip_embed)


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
