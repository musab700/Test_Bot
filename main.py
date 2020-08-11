import json
import random
import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    print('Bot is connected')


@client.event
async def on_message(message):
    with open('logs.txt', 'a') as file:
        file.write(f'{message.author}:{message.content}')
    print(f'{message.author}:{message.content}')


with open("properties.json") as properties:
    data = json.load(properties)

client.run(data.token)
