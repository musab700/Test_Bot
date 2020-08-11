import json
import random
import discord
from discord.ext import commands

client = commands.Bot('.')


@client.event
async def on_ready():
    print('Bot is connected')


# logs messages into logs.txt
@client.event
async def on_message(message):

    if message.author == client.user:
        return
    else:
        with open('logs.txt', 'a') as file:
            file.write(f'{message.author}:{message.content}\n')
            print(f'{message.author}:{message.content}')
        await client.process_commands(message)


# checks client ping
@client.command()
async def ping(ctx):
    await ctx.send(f'Ping: {round(client.latency*1000)}ms')


with open("properties.json") as properties:
    data = json.load(properties)

client.run(data['token'])
