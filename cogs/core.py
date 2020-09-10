import discord
from discord.ext import commands
import json


class Core(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
