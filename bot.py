from modules import discord
import process

class Prefect(discord.Client):
	def __init__(bot, *args, **kwargs):
		super().__init__(intents=discord.Intents.all(), *args, **kwargs)
		bot.__ver__ = process.quickfunctions.f("locale/version")
	
	async def on_ready(bot):
		await process.ready.run(bot)

	async def on_message(bot, message):
		await process.commands.main(message, bot)

	async def on_raw_message_edit(bot, payload):
		await process.commands.edit(payload, bot)

	async def on_raw_reaction_add(bot, payload):
		await process.reactions.run(payload, bot)

	async def on_raw_reaction_remove(bot, payload):
		await process.reactions.run(payload, bot)

