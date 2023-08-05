import discord, random
from importlib import resources
from .utils import blank

def file(num: int=None):
	"""
	Returns a `discord.File()` of a seal for py-cord
	"""
	try:
		if num == None:
			sealrand = f"{random.randrange(1, 82)}"
		else: 
			if not sealrand > 82:
				sealrand = num
			else:
				sealrand = f"{random.randrange(1, 82)}"
		if len(sealrand) == 1:
			sussy = sealrand
			sealrand = "0" + f"{sussy}"
	finally:
		with resources.open_text('randseal', f'00{sealrand}.jpg') as f:
			return discord.File(fp=f.name, filename=f"{sealrand}.png")

randoms = ("Here is your seal!", "Arff Arff!", ":3")

def embed(num: int = ..., title: str = random.choice(randoms)):
	"""
	Returns a `discord.Embed()` of a seal
	"""
	try:
		if num == None:
			sealrand = f"{random.randrange(1, 82)}"
		else: 
			if not sealrand > 82:
				sealrand = num
			else:
				sealrand = f"{random.randrange(1, 82)}"
		if len(sealrand) == 1:
			sussy = sealrand
			sealrand = "0" + f"{sussy}"
	finally:
		embeda = discord.Embed(colour=blank(), title=title).set_image(url=f"https://raw.githubusercontent.com/mariohero24/randseal/main/randseal/00{sealrand}.jpg")
		return embeda

# python3 -m twine upload --repository pypi dist/*