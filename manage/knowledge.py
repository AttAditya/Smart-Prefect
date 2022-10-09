from modules import discord, requests, bs4, json

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
	"meaning": meaning,
	"daily-word": wotd
}

