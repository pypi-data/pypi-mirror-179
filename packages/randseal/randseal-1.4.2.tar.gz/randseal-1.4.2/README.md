# randseal
Simple package that produces a seal image. The image is then output as a `discord.File` for Pycord.

### Usage example
```py
from randseal import get
from discord import Bot, Intents

bot = Bot(intents=Intents.default())

@bot.slash_command()
async def sealimg(ctx):
	await ctx.respond(file=get.file())

@bot.slash_command()
async def sealembed(ctx):
	await ctx.respond(embed=get.embed())

bot.run("token")
```