import json
import discord
from discord.ext import commands

client = commands.Bot(command_prefix='^')

data = {}


@client.event
async def on_ready():
    global data
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
        print("{} connected".format(client.user))
    except FileNotFoundError:
        print("File not found")


@client.command
async def register(ctx):
    user = str(ctx.message.author.id)
    if user not in data:
        data['users'][0][user] = 100;
        with open('data.json', 'w') as f:
            json.dump(data, f)
