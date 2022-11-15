from modules import discord

async def check_voice(ctx, bot):
    voice_state = ctx.author.voice
    my_member_identity = await ctx.author.guild.fetch_member(bot.user.id)
    my_voice_state = my_member_identity.voice

    if voice_state != None:
        voice_channel = voice_state.channel

        my_voice_channel = None
        my_channel_id = None
        if my_voice_state != None:
            my_voice_channel = my_voice_state.channel
            my_channel_id = my_voice_channel.id

        if voice_channel.id == my_channel_id:
            return True
    return False


async def join_my_voice(ctx, args, bot):
    voice_state = ctx.author.voice

    if voice_state != None:
        voice_channel = voice_state.channel

        await voice_channel.connect()
        embed_info = {"title": "Audio System", "color": 0x1db954}
        embed = discord.Embed(**embed_info)

        field1 = {
            "name": "Connection Status",
            "value": f"Joined <#{voice_channel.id}>"
        }
        embed.add_field(**field1)
        await ctx.channel.send(embed=embed)
    else:
        embed_info = {"title": "Audio System", "color": 0xff2e2e}
        embed = discord.Embed(**embed_info)

        field1 = {"name": "Error", "value": "Please join a voice channel."}
        embed.add_field(**field1)
        await ctx.channel.send(embed=embed)


async def leave_my_voice(ctx, args, bot):
    voice_check = await check_voice(ctx, bot)

    if voice_check:
        voice_state = ctx.author.voice
        voice_channel = voice_state.channel
        for voice_client in bot.voice_clients:
            if (voice_client.guild == ctx.guild):
                await voice_client.disconnect()

                embed_info = {"title": "Audio System", "color": 0x1db954}
                embed = discord.Embed(**embed_info)

                field1 = {
                    "name": "Connection Status",
                    "value": f"Disconnect from <#{voice_channel.id}>"
                }
                embed.add_field(**field1)
                await ctx.channel.send(embed=embed)

                break
        else:
            embed_info = {"title": "Audio System", "color": 0xff2e2e}
            embed = discord.Embed(**embed_info)

            field1 = {
                "name": "Error",
                "value": "You are unauthorized for the action."
            }
            embed.add_field(**field1)
            await ctx.channel.send(embed=embed)
    else:
        embed_info = {"title": "Audio System", "color": 0xff2e2e}
        embed = discord.Embed(**embed_info)

        field1 = {
            "name": "Error",
            "value": "You are unauthorized for the action."
        }
        embed.add_field(**field1)
        await ctx.channel.send(embed=embed)


async def spotify(ctx, args, bot):
    embed_info = {"title": "Audio System", "color": 0xecf542}
    embed = discord.Embed(**embed_info)

    field1 = {
        "name": "Not Ready!",
        "value": "This command is under development."
    }
    embed.add_field(**field1)
    await ctx.channel.send(embed=embed)

    command = f"spotdl '{args}'"
    command += " -o resources/music "
    command += "--ignore-ffmpeg-version"

index = {
    "join-my-voice": join_my_voice,
    "leave-my-voice": leave_my_voice,
    "spotify": spotify
}
