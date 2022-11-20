from modules import discord

async def run(bot):
	status = discord.Status.online
	activity = discord.Activity(name="For Knowledge! 🧑‍🎓", type=3)
	presence = {"status": status, "activity": activity}
	await bot.change_presence(**presence)

	print(f"\n{bot.user} is active now...\n")

