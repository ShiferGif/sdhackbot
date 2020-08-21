import discord
from discord.ext import commands

client = commands.Bot( command_prefix = '.' )
# .hello

@client.event

async def on_ready():
	print( 'Bot ready' )

	await client.change_presence( status = discord.Status.idle,activity = discord.Game( 'sdhack > best cheat' ) )

@client.command( pass_context = True )

async def verify( ctx ):
	author = ctx.message.author
	await ctx.send( F' Hello, {author.mention} https://discord.gg/KvemM5f this is a link, you can read faq or ask a question :3 https://cdn.discordapp.com/attachments/746332648946925639/746338458389315584/09212d9a7f45a53d88a8bfe0c67b8d54.png' )

# Connect

token = NzQ2Mjg0NDcyNTgzOTc5MDE5.Xz-Fkw.NXs1Ai9wnxcakCqAgy-mFGw1XAI

client.run( token )