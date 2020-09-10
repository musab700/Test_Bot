import discord
from discord.ext import commands
import random
import json


class Economy(commands.Cog):
    def __int__(self, bot):
        self.bot = bot

    @commands.command()
    async def coinflip(self, ctx, arg1):
        outcome = random.randint(0, 1)
        if arg1 == "h" or "t":
            if (arg1 == "h" and outcome == 0) or (arg1 == "t" and outcome == 1):
                await ctx.send("You win")
            else:
                await ctx.send("You lose")
        else:
            await ctx.send("Invalid usage")


def setup(bot):
    bot.add_cog(Economy(bot))
