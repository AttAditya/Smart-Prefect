from modules import discord, os
from process.quickfunctions import f, w
import process

bot = discord.Client(intents=discord.Intents.all())

prefixes = f("locale/prefix").split("\n")


@bot.event
async def on_ready():
    status = discord.Status.online
    activity = discord.Activity(
        name="For Knowledge! 🧑‍🎓",
        type=3
    )
    presence = {
        "status": status,
        "activity": activity
    }

    await bot.change_presence(**presence)
    
    print(f"\n{bot.user} is active now...\n")
    
    w("locale/error.html", "w", "")
    process.web.start()


@bot.event
async def on_message(message):
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

        data = [
            message,
            command,
            args,
            bot
        ]

        await process.commands.run(*data)


@bot.event
async def on_raw_reaction_add(payload):
    await process.reactions.run(payload, bot)

@bot.event
async def on_raw_reaction_remove(payload):
    await process.reactions.run(payload, bot)


if not(f("token")):
    token = os.environ["TOKEN"]
else:
    token = f("token")

try:
    if not(f"webdev"):
        bot.run(token)
    else:
        process.web.start()
except:
    process.web.start()
