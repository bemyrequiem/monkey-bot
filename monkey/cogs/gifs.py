def __init__(bot):
    monkey_gif(bot)

def monkey_gif(bot):
    @bot.command(aliases=['mg'])
    async def monkeygif(ctx, top_text, bottom_text):
        await ctx.send(f"monkey gif - top: {top_text}, bottom: {bottom_text}")