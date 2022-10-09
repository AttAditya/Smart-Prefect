from modules import discord

async def ping(ctx, args, bot):
    await ctx.channel.send(f"PING! (Latency: {int(bot.latency*1000)/1000}ms)")


async def embed_message(ctx, args, bot):
    parts = args.split("\n")
    m_color = discord.Color.from_str(parts[0]) if len(parts) > 1 else 0xffffff
    m_title = parts[1] if len(parts) > 2 else ctx.guild.name
    m_desc = parts[2] if len(parts) > 3 else None
    m_fname = parts[3] if len(parts) > 4 else "Message"
    m_content = "\n".join(parts[4:]) if len(parts) > 4 else ""

    embed_info = {"title": m_title, "color": m_color, "description": m_desc}
    embed = discord.Embed(**embed_info)

    field1 = {"name": m_fname, "value": m_content}
    embed.add_field(**field1)

    wh = await ctx.channel.create_webhook(name="Service")

    await wh.send(embed=embed,
                  username=ctx.author.name,
                  avatar_url=ctx.author.avatar.url)
    await wh.delete()

    await ctx.delete()

async def interest_poll(ctx, args, bot):
    m_color = 0xbf96ff
    m_title = "Polls"
    m_fname = "Interest Poll"
    m_content = args if args else "Random Interest Poll"

    embed_info = {"title": m_title, "color": m_color}
    embed = discord.Embed(**embed_info)

    field1 = {"name": m_fname, "value": m_content}
    embed.add_field(**field1)

    m = await ctx.channel.send(embed=embed)
    await m.add_reaction("👍")

    await ctx.delete()

async def yn_poll(ctx, args, bot):
    m_color = 0xbf96ff
    m_title = "Polls"
    m_fname = "Yes No Poll"
    m_content = args if args else "Random Yes No Poll"

    embed_info = {"title": m_title, "color": m_color}
    embed = discord.Embed(**embed_info)

    field1 = {"name": m_fname, "value": m_content}
    embed.add_field(**field1)

    m = await ctx.channel.send(embed=embed)
    await m.add_reaction("✔️")
    await m.add_reaction("✖️")

    await ctx.delete()

index = {
    "ping": ping,
    "embed": embed_message,
    "interest-poll": interest_poll,
    "yn-poll": yn_poll
}
