from modules import os
from process.quickfunctions import f

import process.commands as commands
import process.reactions as reactions
import process.ready as ready
import process.quickfunctions as quickfunctions
import process.database as database

import bot as smart_prefect_bot

def run(*args, **kwargs):
	database.load()
	bot = smart_prefect_bot.Prefect()

	token = ""
	if not (f("token")):
		token = os.environ["TOKEN"]
	else:
		token = f("token")

	try:
		if not (f("webdev")):
			bot.run(token)
	except:
		pass

