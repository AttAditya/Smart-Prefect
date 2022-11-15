from modules import discord
from process.quickfunctions import w
import process.web

async def run(bot):
	status = discord.Status.online
	activity = discord.Activity(name="For Knowledge! 🧑‍🎓", type=3)
	presence = {"status": status, "activity": activity}

	await bot.change_presence(**presence)

	print(f"\n{bot.user} is active now...\n")

	w("locale/error.html", "w", "")
	process.web.start()

