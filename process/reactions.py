from modules import discord
from process.quickfunctions import f

async def check_permission(user, channel, permissions):
    required = []
    available = {
        "admin": user.guild_permissions.administrator,
        "channels": user.guild_permissions.manage_channels,
        "guild": user.guild_permissions.manage_guild,
        "roles": user.guild_permissions.manage_roles,
        "messages": user.guild_permissions.manage_messages
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
            "value": "You do not have permissions."
        }
        embed.add_field(**field1)

        await channel.send(embed=embed)

        return False
    return True

async def run(payload, bot):
	emoji = payload.emoji
	msg_id = payload.message_id
	guild = bot.get_guild(payload.guild_id)
	user = guild.get_member(payload.user_id)
	channel = guild.get_channel(payload.channel_id)

	if user.bot:
		return

	rxn_data = {}
	raw_rxn_data = f("locale/roles")

	for raw_msg_data in raw_rxn_data.split("\n")[:-1]:
		temp_msg_id = raw_msg_data.split(":")[0]
		temp_role_id = raw_msg_data.split(":")[1]
		rxn_data.update({
			int(temp_msg_id): int(temp_role_id)
		})
	
	if msg_id in rxn_data:
		role = guild.get_role(rxn_data[msg_id])
		try:
			if payload.event_type == "REACTION_ADD":
				await user.add_roles(role)
			elif payload.event_type == "REACTION_REMOVE":
				await user.remove_roles(role)
		except:
			pass
		return
	
	if emoji.name == "🗑️":
		try:
			msg = await channel.fetch_message(msg_id)

			perms = ["admin", "messages"]
			cp = [user, channel, perms]
			permit = await check_permission(*cp)
			if permit:
				await msg.delete()
			else:
				return
		except:
			pass

