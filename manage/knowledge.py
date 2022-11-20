from modules import discord, requests, bs4, json, math
from math import *

async def function_names(ctx, args, bot):
	content = ""
	functions = [f for f in dir(math) if not(f.startswith("_"))]

	content = ", ".join(functions)
	content = f"```csv\n{content}```"
	content += "\n**NOTE**: If you passed name of a function and this appears, the function might not be available. You can also try removing spaces if any after command name."

	if args in functions:
		if hasattr(getattr(math, args), "__text_signature__"):
			content = str(getattr(math, args).__text_signature__)
			content = content.replace(" ", "").split(",")[1:-1]
			content = ", ".join(content)
			content = f"**Function**: {args}({content})\n"
			content += f"**Description**: {str(getattr(math, args).__doc__)}"
		else:
			content = f"**Special Value**: {args}\n"
			content += f"**Description**: {str(getattr(math, args))}"

	embed_info = {
		"title": "Knowledge",
		"color": 0xffe099
	}
	embed = discord.Embed(**embed_info)

	field1 = {
		"name": "All Math Functions Available To Use With Calculate",
		"value": content
	}
	embed.add_field(**field1)

	await ctx.channel.send(embed=embed)

async def calculator(ctx, args, bot):
	content = ""
	try:
		content = eval(args if args.replace(" ", "") != "" else "0")
		args_ = args.replace("*", "\\*")
		content = f"**Expression**: {args_}\n**Result**: *`{content}`*"
	except:
		content = f"**Expression**: {args}\n**Result**: *Error! Please check you expression...*"

	embed_info = {
		"title": "Knowledge",
		"color": 0xffe099
	}
	embed = discord.Embed(**embed_info)

	field1 = {
		"name": "Calculator",
		"value": content
	}
	embed.add_field(**field1)

	await ctx.channel.send(embed=embed)

async def wotd(ctx, args, bot):
	embed_info = {
		"title": "Knowledge",
		"color": 0xffe099
	}
	embed = discord.Embed(**embed_info)

	site = "https://www.merriam-webster.com/"
	site += "word-of-the-day/calendar"

	site_data = requests.get(site)
	site_data = site_data.text

	soup = bs4.BeautifulSoup(
		site_data,
		features="html.parser"
	)
	word = soup.h2.get_text()
	word_def = soup.p.get_text()

	content = f"> ***{word}***\n"
	content += f"**Meaning**: *{word_def}*\n"
	content += "\n**Source**: [Merriam Webster]"
	content += f"({site})"

	field1 = {
		"name": "Word of the Day",
		"value": content
	}
	embed.add_field(**field1)

	await ctx.channel.send(embed=embed)

async def meaning(ctx, args, bot):
	embed_info = {
		"title": "Knowledge",
		"color": 0xffe099
	}
	embed = discord.Embed(**embed_info)

	word = ""
	word_def = ""

	for raw_word in args.split(" "):
		if raw_word:
			word = raw_word.lower()
			break
	else:
		word = "ERROR"
		word_def = "Please provide a word!"
	
	if word.lower() == word:
		site = "https://api.dictionaryapi.dev/api/v2/"
		site += "entries/en/"
		site += word

		site_data = requests.get(site)
		site_data = site_data.text

		word_data = json.loads(site_data)

		try:
			meanings = word_data[0]["meanings"]
		except:
			meanings = []
			word += "* - ERROR** *"
			word_def += "Word not available. "
			word_def += "Please check the word. "
			word_def += "The spelling might be wrong. "

		for meaning in meanings:
			usage = meaning["partOfSpeech"]
			definitions = meaning["definitions"]

			word_def += "**> Part of Speech: "
			word_def += f"*{usage}***"
			if len(definitions) >= 3:
				definitions = definitions[:3]
				word_def += " (*top definitions*)"
			word_def += "\n"
			
			for i, d in enumerate(definitions):
				word_def += f"**Definition {i+1}:**\n"
				word_def += f"{d['definition']}\n\n"
		
		if len(meanings) > 0:
			word_def += "**Source**: [Free Dictionary API]"
			word_def += f"({site})"

	field1 = {
		"name": f"Meaning - *{word}*",
		"value": word_def
	}
	embed.add_field(**field1)

	await ctx.channel.send(embed=embed)

index = {
	"calculate": calculator,
	"functions": function_names,
	"meaning": meaning,
	"daily-word": wotd
}

