mport interactions

bot = interactions.Client(token)

@bot.command(

    name="hello",

    description="hello, how are you?",

    scope=896655023600185344,)

async def my_first_command(ctx: interactions.CommandContext):

    await ctx.send("Hi there!")

bot.start()
