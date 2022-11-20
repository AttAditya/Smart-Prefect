from modules import discord
from process.quickfunctions import w

embed_info = {"title": "Server Management", "color": 0xecf542}

channel_permissions = ["admin", "channels", "guild"]
roles_permissions = ["admin", "roles"]

async def check_permission(ctx, permissions):
	author = await ctx.guild.fetch_member(ctx.author.id)

	required = []
	available = {
		"admin": author.guild_permissions.administrator,
		"channels": author.guild_permissions.manage_channels,
		"guild": author.guild_permissions.manage_guild,
		"roles": author.guild_permissions.manage_roles,
		"messages": author.guild_permissions.manage_messages
	}

	for permission in permissions:
		if permission in available:
			required.append(available[permission])

	permit = False
	for satisfying in required:
		if satisfying:
			permit = True
			break

	if not permit:
		embed = discord.Embed(**embed_info)
		embed.color = 0xff2e2e

		field1 = {
			"name": "Error",
			"value": "You do not have permissions to manage server."
		}
		embed.add_field(**field1)

		await ctx.channel.send(embed=embed)

		return False
	return True


async def clone_this_channel(ctx, args, bot):
	permit = await check_permission(ctx, channel_permissions)
	if not permit:
		return

	cloned_channel = await ctx.channel.clone()

	embed = discord.Embed(**embed_info)

	field1 = {
		"name": "Clone Channel",
		"value": f"Channel Cloned Successfully: <#{cloned_channel.id}>"
	}
	embed.add_field(**field1)

	await cloned_channel.send(embed=embed)


async def create_channel(ctx, args, bot):
	permit = await check_permission(ctx, channel_permissions)
	if not permit:
		return
	
	if len(args.split(" ")) < 2:
		if len(args.replace(" ", "")) != 0:
			embed = discord.Embed(**embed_info)
			embed.color = 0xff2e2e

			field1 = {
				"name": "Error",
				"value": "Name was not given."
			}
			embed.add_field(**field1)

			await ctx.channel.send(embed=embed)

			return
		else:
			embed = discord.Embed(**embed_info)
			embed.color = 0xff2e2e

			field1 = {
				"name": "Error",
				"value": "Type was not given. Available types to create: `Text`, `Voice`, `Stage`, `Forum`, `Category`"
			}
			embed.add_field(**field1)

			await ctx.channel.send(embed=embed)

			return
	
	channel_type = args.split(" ")[0].lower()
	channel_name = " ".join(args.split(" ")[1:])

	channel = ctx.channel
	guild = channel.guild
	category = guild

	if hasattr(channel, "category"):
		category = channel.category

	try:
		if channel_type == "text":
			channel = await category.create_text_channel(channel_name)
		elif channel_type == "voice":
			channel = await category.create_voice_channel(channel_name)
		elif channel_type == "stage":
			channel = await category.create_stage_channel(channel_name, "...")
		elif channel_type == "forum":
			channel = await category.create_forum(channel_name)
		elif channel_type == "category":
			channel = await guild.create_category(channel_name)
			await channel.create_voice_channel(f"{channel_name} Voice")
			channel = await channel.create_text_channel(f"{channel_name} Chat")
		else:
			embed = discord.Embed(**embed_info)
			embed.color = 0xff2e2e

			field1 = {
				"name": "Error",
				"value": "Type was invalid. Available types to create: `Text`, `Voice`, `Stage`, `Forum`, `Category`"
			}
			embed.add_field(**field1)

			await ctx.channel.send(embed=embed)

			return

		embed = discord.Embed(**embed_info)

		channel_type = f"{channel_type[0].upper()}{channel_type[1:].lower()}"

		field1 = {
			"name": "Create Channel",
			"value": f"{channel_type} Channel Created Successfully: <#{channel.id}>"
		}
		embed.add_field(**field1)

		await ctx.channel.send(embed=embed)
	except:
		embed = discord.Embed(**embed_info)
		embed.color = 0xff2e2e

		field1 = {
			"name": "Error",
			"value": "Some unknown error occured."
		}
		embed.add_field(**field1)

		await ctx.channel.send(embed=embed)

		return


async def reset_this_channel(ctx, args, bot):
	permit = await check_permission(ctx, channel_permissions)
	if not permit:
		return

	cloned_channel = await ctx.channel.clone()
	await ctx.channel.delete()

	embed = discord.Embed(**embed_info)

	field1 = {
		"name": "Reset Channel",
		"value": f"Channel Resetted Successfully: <#{cloned_channel.id}>"
	}
	embed.add_field(**field1)

	await cloned_channel.send(embed=embed)


async def delete_this_channel(ctx, args, bot):
	permit = await check_permission(ctx, channel_permissions)
	if not permit:
		return

	await ctx.channel.delete()


async def reaction_role(ctx, args, bot):
	permit = await check_permission(ctx, roles_permissions)
	if not permit:
		return

	contents = args.split(" ")
	if len(contents) < 1:
		embed = discord.Embed(**embed_info)
		embed.color = 0xff2e2e

		field1 = {"name": "Error", "value": "Argument Missing: `<role>`"}
		embed.add_field(**field1)

		await ctx.channel.send(embed=embed)
	else:
		role_raw = contents[0]
		role_raw = role_raw.replace("<", "")
		role_raw = role_raw.replace(">", "")
		role_raw = role_raw.replace("@", "")
		role_raw = role_raw.replace("&", "")
		role_id = 0

		try:
			role_id = int(role_raw)
		except:
			role_id = 0

		if role_id:
			role = ctx.guild.get_role(role_id)

			if role != None:
				embed = discord.Embed(**embed_info)
				embed.color = 0x66f542

				field1 = {
					"name": "Roles",
					"value": f"React to get role: <@&{role.id}>"
				}
				embed.add_field(**field1)

				m = await ctx.channel.send(embed=embed)
				await m.add_reaction("👍")

				w("locale/roles", "a", f"{m.id}:{role.id}\n")

				return

		embed = discord.Embed(**embed_info)
		embed.color = 0xff2e2e

		field1 = {
			"name":
			"Error",
			"value":
			f"Role not found: {role_raw}\nPlease try using role id or mentioning role correctly."
		}
		embed.add_field(**field1)

		await ctx.channel.send(embed=embed)

index = {
	"create-channel": create_channel,
	"clone-this-channel": clone_this_channel,
	"reset-this-channel": reset_this_channel,
	"delete-this-channel": delete_this_channel,
	"reaction-role": reaction_role
}
