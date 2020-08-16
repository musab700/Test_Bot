import json
import random
import discord
from discord.ext import commands

client = commands.Bot(command_prefix="`")

data = {}


@client.event
async def on_ready():
    global data
    with open('data.json') as file:
        data = json.load(file)
    print("{} connected".format(client.user))


@client.command()
async def ping(ctx):
    ping_embed = discord.Embed(title="Ping: {}ms".format(round(client.latency*1000)))
    await ctx.send(embed=ping_embed)


@client.command()
async def cf(ctx, arg):
    h_or_t = random.randint(0, 1)
    coinflip_embed = discord.Embed()
    if arg == 'h':
        if h_or_t == 0:
            coinflip_embed.title = "{} You win it was heads".format(ctx.message.author.mention)
            await ctx.send(embed=coinflip_embed)
        else:
            coinflip_embed.title = "{} You lose it was tails".format(ctx.message.author.mention)
            await ctx.send(embed=coinflip_embed)
    elif arg == 't':
        if h_or_t == 1:
            coinflip_embed.title = "{} You win, it was tails".format(ctx.message.author.mention)
            await ctx.send(embed=coinflip_embed)
        else:
            coinflip_embed.title = "{} You lose, it was heads".format(ctx.message.author.mention)
            await ctx.send(embed=coinflip_embed)
    else:
        coinflip_embed.title = "Invalid usage"
        await ctx.send(embed=coinflip_embed)


@client.command()
async def register(ctx):
    register_embed = discord.Embed()
    user = str(ctx.message.author.id)
    if user not in data:
        data[user] = 100
        with open('data.json', 'w') as f:
            json.dump(data, f)
        register_embed.title = "You're registered!"
        await ctx.send(embed=register_embed)
    else:
        register_embed.title = "You're already registered"
        await ctx.send(embed=register_embed)


with open('properties.json') as properties:
    token = json.load(properties)

client.run(token['token'])
