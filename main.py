import json
import random
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
async def on_member_join(member, channel):
    await channel.send(f'{member} joined')
    print(f'{member} has joined')


@client.event
async def on_member_remove(member, channel):
    await channel.send(f'{member} left')
    print(f'{member} has joined')

# Writes the messages in log.txt and displays them in console


@client.event
async def on_message(message):
    await client.process_commands(message)
    if message.author == client:
        return
    else:
        with open('logs.txt', 'a') as file:
            file.write(f'{message.author}: {message.content} \n')
            print(f'{message.author}:{message.content}')


# ____ Commands section ____

@client.command()
async def ping(message):
    await message.channel.send(f'Pong: {round(client.latency * 1000)} ms')


@client.command()
async def coinf(message):
    num = random.randint(0, 1)
    if num == 0:
        await message.channel.send('Heads')
    else:
        await message.channel.send('Tails')

with open("properties.json") as properties:
    data = json.load(properties)

client.run(data["token"])
