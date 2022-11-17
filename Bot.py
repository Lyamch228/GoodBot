import discord

import interactions

from discord.ext import commands

bot = interactions.Client((os.getenv('TOKEN')))

@bot.command(

    name="hello",

    description="hello, how are you?",

    scope=896655023600185344,)

async def my_first_command(ctx: interactions.CommandContext):

    await ctx.send("Hi there!")

@bot.command(

    name="serverinfo",

    description="server info",

    scope=896655023600185344,)

async def (ctx: interactions.CommandContext):

	

bot.start()
