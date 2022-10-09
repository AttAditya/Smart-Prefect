from modules import discord, os
from process.quickfunctions import f

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

    field1 = {"name": "Status", "value": f("locale/status")}
    embed.add_field(**field1)

    await ctx.channel.send(embed=embed)

index = {
    "command-names": command_names,
    "help": help_with,
    "status": status
}
