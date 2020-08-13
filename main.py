import json
import random
import discord
from discord.ext import commands

client = commands.Bot(command_prefix='|')

ye_counter = 0


@client.event
async def on_ready():
    print('Bot is connected')


@client.command()
async def yecnter(ctx):
    await ctx.send("{} ye's ye'd".format(ye_counter))


# checks client ping
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


with open("properties.json") as properties:
    data = json.load(properties)

client.run(data['token'])
