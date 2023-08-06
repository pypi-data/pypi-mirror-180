import discord
import aiohttp
import requests
import random
import io
from importlib import metadata


class Client:
	"""
	The client class for the randseal package containing everything (new in version 2.0.0)
	"""
	def __init__(self, session: aiohttp.ClientSession = None, session2: aiohttp.ClientSession = None):
		self.session = aiohttp.ClientSession(auto_decompress=False) or session
		self.session2 = aiohttp.ClientSession() or session2

	async def asyncFile(self):
		"""
		Returns a `discord.File()` of a seal for py-cord in a non-blocking way (new in version 2.0.0)
		"""
		try:
			try:
				sealrand = f"{random.randrange(1, 82)}"
			finally:
				if len(sealrand) == 1:
					sussy = sealrand
					sealrand = "0" + f"{sussy}"
		finally:
			async with self.session.get(f"https://raw.githubusercontent.com/mariohero24/randseal/fbba6657532d0b6db21c91986843a08a7ab19f26/randseal/00{sealrand}.jpg") as r:
				hi = io.BytesIO(await r.read())
				return discord.File(fp=hi, filename=sealrand + ".jpg")

	def File(self):
		"""
		Returns a `discord.File()` of a seal for py-cord in a potentially blocking way (classic)
		"""
		try:
			try:
				sealrand = f"{random.randrange(1, 82)}"
			finally:
				if len(sealrand) == 1:
					sussy = sealrand
					sealrand = "0" + f"{sussy}"
		finally:
			r = requests.get(
				f"https://raw.githubusercontent.com/mariohero24/randseal/fbba6657532d0b6db21c91986843a08a7ab19f26/randseal/00{sealrand}.jpg", stream=True)
			return discord.File(fp=io.BytesIO(r.content), filename=sealrand + ".jpg")

	def Embed(self, title: str = None):
		"""
		Returns a `discord.Embed()` of a seal which can be edited or used in a message
		"""
		try:
			try:
				sealrand = f"{random.randrange(1, 82)}"
			finally:
				if len(sealrand) == 1:
					sussy = sealrand
					sealrand = "0" + f"{sussy}"
		finally:
			if title != None:
				return discord.Embed(colour=Client.blank, title=title).set_image(url=f"https://raw.githubusercontent.com/mariohero24/randseal/fbba6657532d0b6db21c91986843a08a7ab19f26/randseal/00{sealrand}.jpg")
			else:
				return discord.Embed(colour=Client.blank).set_image(url=f"https://raw.githubusercontent.com/mariohero24/randseal/fbba6657532d0b6db21c91986843a08a7ab19f26/randseal/00{sealrand}.jpg")

	async def fetchrole(self, context, id: discord.object.SupportsIntCast) -> discord.Role:
		"""
		Returns a `discord.Role` that is really just a `discord.Object` for easy use, decided not to edit the class itself because it would be a nightmare to fix (reworked in v2.2.0)
		"""
		return discord.Object(id)

	blank = 0x2f3136
	"""A colour exactly like a `discord.Embed` (reworked in version 2.1.0)"""


__author__: str = "Guard Boi"
"""The author of the package"""

__description__: str = "Generates a random seal image for py-cord"
"""A short description of the package"""

__licence__: str = "MIT"
"""The licence type of the package"""

__version__ = metadata.version("randseal")
"""The version of the package"""

# python3 -m twine upload --repository pypi dist/*
