import discord
from discord.ext import commands
from youtube_dl import YoutubeDL


def run_discord_bot():
    TOKEN = 'MTA3NTEyMzY1NTE2MTQxMzc5NQ.Gv0E7f.5FAJY86q0U0P-nRln9lVnHzzTVcftxqFCYUXvU'

    intents = discord.Intents.all()
    client = commands.Bot(command_prefix="/", intents=intents)

    @client.command()
    async def join(ctx):
        if ctx.author.voice:
            channel = ctx.author.voice.channel
            await channel.connect()
            await ctx.send(f'{client.user.name} connected to {ctx.author.voice.channel}')

        else:
            await ctx.send("You must be in voice channel first !")

    @client.command(name='leave')
    async def leave(ctx):
        if ctx.voice_client:
            await ctx.guild.voice_client.disconnect()
            await ctx.send(f'{client.user.name} disconnected!')
        else:
            await ctx.send(f'{client.user.name} is not in any channel!')

    def search_song_in_youtube(song):
        YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
        with YoutubeDL(YDL_OPTIONS) as ydl:
            found_song = ydl.extract_info(f"ytsearch:{song}", download=False,)
            return found_song

    @client.command(name='play')
    async def play(ctx, url):
        if ctx.voice_client:
            song = search_song_in_youtube(url)
            print(song)
            await ctx.send(f"Currently cannot play music!")
        await ctx.send(f'{client.user.name} must be in a channel to play music!')

    client.run(TOKEN)

