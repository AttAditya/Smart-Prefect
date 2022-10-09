import manage

async def run(ctx, command: str, args, bot):
    if command in manage.command_data:
        await manage.command_data[command](ctx, args, bot)

        try:
            await ctx.delete()
        except:
            pass

