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
    if message.author == client:
        return
    else:
        with open('logs.txt', 'a') as file:
            file.write(f'{message.author}: {message.content} \n')
            print(f'{message.author}:{message.content}')


client.run('NzI1NTE3NDI2NzExNTkzMjg0.XvP4wQ._6k0C5HAwT8tDsI5HOizJGP1oGU')
