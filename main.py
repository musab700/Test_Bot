import discord
from discord.ext import commands
import json


client = commands.Bot(command_prefix="?")
client.load_extension("cogs.economy")


@client.event
async def on_ready():
    print("{} connected".format(client.user))


with open("properties.json") as properties:
    prop = json.load(properties)

TOKEN = prop['token']

client.run(TOKEN)
