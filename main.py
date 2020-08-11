import json
import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.')


@client.event
async def on_disconnect():
    print("Bot disconnected")


@client.event
async def on_ready():
    print("Bot is connected")


@client.event
async def on_member_join(member):
    print(f'{member} has joined')


@client.event
async def on_member_remove(member):
    print(f'{member} has left')


@client.event
async def on_message(message):
    await client.process_commands(message)
    if message.author == client:
        return
    else:
        with open('logs.txt', 'a') as file:
            file.write(f'{message.author}: {message.content} \n')
            print(f'{message.author}:{message.content}')


@client.command()
async def ping(message):
    await message.channel.send(f'Pong: {message.author.latency}')

with open("properties.json") as properties:
    data = json.load(properties)
client.run(data["token"])
