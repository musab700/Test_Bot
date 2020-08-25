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
    ping_embed = discord.Embed(title="Ping: {}ms".format(round(client.latency * 1000)), color=0xff6737)
    await ctx.send(embed=ping_embed)


@client.command()
async def bal(ctx):
    user_id = str(ctx.author.id)
    bal_embed = discord.Embed(color=0xff6737)
    if user_id not in data:
        data[user_id] = 100
        with open('data.json', 'w') as f:
            json.dump(data, f)
        bal_embed.title = "You have {} points".format(data[user_id])
        await ctx.send(embed=bal_embed)
    else:
        bal_embed.title = "You have {} points".format(data[user_id])
        await ctx.send(embed=bal_embed)


@client.command()
async def cf(ctx, arg, amounts: int):
    user_id = str(ctx.author.id)
    coinflip_embed = discord.Embed(color=0xff6737)
    if user_id not in data:
        data[user_id] = 100
        with open('data.json', 'w') as f:
            json.dump(data, f)
    elif amounts <= data[user_id]:
        h_or_t = random.randint(0, 1)
        with open('data.json', 'w') as cf_file:
            if arg == 'h':
                if h_or_t == 0:
                    coinflip_embed.title = f"You won {amounts}, it was heads"
                    await ctx.send("{}".format(ctx.message.author.mention), embed=coinflip_embed)
                    data[user_id] += amounts
                    json.dump(data, cf_file)
                else:
                    coinflip_embed.title = f"You lost {amounts}, it was tails"
                    await ctx.send("{}".format(ctx.message.author.mention), embed=coinflip_embed)
                    data[user_id] -= amounts
                    json.dump(data, cf_file)
            elif arg == 't':
                if h_or_t == 1:
                    coinflip_embed.title = f"You won {amounts}, it was tails"
                    await ctx.send("{}".format(ctx.message.author.mention), embed=coinflip_embed)
                    data[user_id] += amounts
                    json.dump(data, cf_file)
                else:
                    coinflip_embed.title = f"You lost {amounts}, it was heads"
                    await ctx.send("{}".format(ctx.message.author.mention), embed=coinflip_embed)
                    data[user_id] -= amounts
                    json.dump(data, cf_file)
            else:
                coinflip_embed.title = "Invalid usage"
                await ctx.send(embed=coinflip_embed)
    else:
        coinflip_embed.title = "You do not have enough balance"
        await ctx.send(embed=coinflip_embed)


@client.command()
@commands.cooldown(1, 3600, commands.BucketType.user)
async def pet(ctx):
    user_id = str(ctx.author.id)
    pet_amount = random.randint(100, 1000)
    pet_embed = discord.Embed(color=0xff6737)
    pet_embed.title = "You earned {} from petting".format(pet_amount)
    data[user_id] += pet_amount
    await ctx.send(embed=pet_embed)
    with open('data.json') as h_file:
        json.dump(data, h_file)


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        cooldown_embed = discord.Embed(color=0xff6737)
        cooldown_embed.title = "You can pet again in {} minutes".format(round(error.retry_after / 60))
        await ctx.send(embed=cooldown_embed)


with open('properties.json') as properties:
    token = json.load(properties)

client.run(token['token'])
