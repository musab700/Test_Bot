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
    await ctx.send(f'Ping: {round(client.latency * 1000)}ms')


@client.command()
async def cf(ctx, arg):
    num = random.randint(0, 1)
    if arg == 'h' or arg == 't':
        if arg == 'h' and num == 0:
            await ctx.send("It was heads, you win!")
        elif arg == 'h' and num == 1:
            await ctx.send("It was tails, you lose!")
        elif arg == 't' and num == 0:
            await ctx.send("It was heads, you lose!")
        else:
            await ctx.send("It was tails, you win!")
    elif arg == "help":
        await ctx.send("Usage: .cf h/t")
    else:
        return


with open("properties.json") as properties:
    data = json.load(properties)

client.run(data['token'])
