# randseal
Simple package that produces a seal image. The image is then output as a `discord.File` for Pycord.

### Usage examples
```py
import randseal
import discord

bot = discord.Bot(intents=discord.Intents.default())

@bot.slash_command()
async def sealimg(ctx):
	await ctx.respond(file=ranseal.file())

@bot.slash_command()
async def sealembed(ctx, title):
	embed = discord.Embed(colour=randseal.utils.blank(), title=title)
	await ctx.respond(embed=ranseal.embed(embed=embed))

bot.run("token")
```