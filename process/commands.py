import manage
from process.quickfunctions import f, bot_prefixes

async def edit(payload, bot):
    guild = await bot.fetch_guild(payload.guild_id)
    channel = await guild.fetch_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)

    await main(message, bot)

async def main(message, bot):
    prefixes = []
    for prefix_set in bot_prefixes().values():
        for prefix in prefix_set:
            prefixes.append(prefix)

    if message.author == bot.user:
        return

    is_command = False
    used_prefix = ""
    for prefix in prefixes:
        if message.content.lower().startswith(prefix):
            is_command = True
            used_prefix = prefix
            break

    if is_command:
        content = message.content
        content = content.replace(used_prefix, "", 1)
        command = content.lower().split(" ")[0]
        args = " ".join(content.split(" ")[1:])

        data = [message, command, args, bot]

        await run(*data)

async def run(ctx, command: str, args, bot):
    if command in manage.command_data:
        await manage.command_data[command](ctx, args, bot)

        try:
            await ctx.delete()
        except:
            pass

