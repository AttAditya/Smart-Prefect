from modules import discord, os, socket
from process.quickfunctions import f, bot_prefixes

async def command_names(ctx, args, bot):
	embed_info = {"title": "Information", "color": 0x66f542}
	embed = discord.Embed(**embed_info)

	all_commands = ", ".join(os.listdir('help'))

	field1 = {"name": "All Commands", "value": f"```{all_commands}```"}
	embed.add_field(**field1)

	await ctx.channel.send(embed=embed)


async def help_with(ctx, args, bot):
	embed_info = {"title": "Information", "color": 0x66f542}
	embed = discord.Embed(**embed_info)

	field1 = {
		"name": f"Help Guide{' - ' + args if args.strip(' ') != '' else ''}",
		"value": f(f"help/{args if args in os.listdir('help') else 'help'}")
	}
	embed.add_field(**field1)

	await ctx.channel.send(embed=embed)


async def status(ctx, args, bot):
	embed_info = {"title": "Information", "color": 0x66f542}
	embed = discord.Embed(**embed_info)

	status_data = f"**Version**: {bot.__ver__}\n**Host**: {socket.gethostname()}\n**Latency**: {int(bot.latency*1000)}ms\n**Status**: {bot.status}"

	field1 = {"name": "Status", "value": status_data}
	embed.add_field(**field1)

	await ctx.channel.send(embed=embed)


async def whatsnew(ctx, args, bot):
	embed_info = {"title": "Information", "color": 0x66f542}
	embed = discord.Embed(**embed_info)

	field1 = {"name": "What's New!", "value": f("locale/whatsnew")}
	embed.add_field(**field1)

	await ctx.channel.send(embed=embed)


async def show_prefixes(ctx, args, bot):
	embed_info = {"title": "Information", "color": 0x66f542}
	embed = discord.Embed(**embed_info)

	prefixes_data = bot_prefixes()
	prefix_ouput = ""

	category_names = {
		"r" : "Recommended",
		"c" : "Common",
		"g" : "General"
	}

	for category in prefixes_data:
		prefixes = prefixes_data[category]
		category_name = ""

		if category in category_names:
			category_name = category_names[category]
		else:
			category_name = "Other Categories"
		
		prefix_ouput += category_name
		prefix_ouput += ":\n`"
		prefix_ouput += "`\n`".join(prefixes)
		
		prefix_ouput += "`\n\n"

	field1 = {"name": "Prefixes", "value": prefix_ouput}
	embed.add_field(**field1)

	await ctx.channel.send(embed=embed)

index = {
	"command-names": command_names,
	"help": help_with,
	"status": status,
	"prefixes": show_prefixes,
	"whatsnew": whatsnew
}
