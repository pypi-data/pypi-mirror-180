import aiohttp
import aiofiles
import json
from importlib import metadata
import yarl

class Link:
	"""
	The :class:`Link` class for the `advlink` package containing your :prop:`url`.
	"""
	def __init__(self, url: str, session: aiohttp.ClientSession = None, session2: aiohttp.ClientSession = None):
		self.session = aiohttp.ClientSession(auto_decompress=False) or session
		self.session2 = aiohttp.ClientSession() or session2
		self.__link__ = url

	async def img(self):
		"""Fetches an image from the url."""
		async with self.session.get(self.url) as r:
			return r.read()

	async def json(self, dict: bool=False):
		"""Fetches a json instance from the url."""
		async with self.session2.get(self.url) as r:
			if dict:
				return json.loads(await r.json())
			else:
				return str(await r.json())

	async def text(self):
		"""Fetches a :class:`str` from the url."""
		async with self.session2.get(self.url) as r:
			return r.text()

	@property
	def url(self):
		return self.__link__

	async def savestr(self, fp: str):
		"""Saves a link's text to a file"""
		async with aiofiles.open(fp, "w") as f:
			async with self.session2.get(self.url) as r:
				return f.write(await r.text())

	async def saveimg(self, fp: str):
		"""Saves the link's image to a file"""
		async with aiofiles.open(fp, "wb") as f:
			async with self.session.get(self.url) as r:
				return f.write(await r.real_url)

	@property
	def yarlURL(self):
		return yarl.URL(self.url)

__author__: str = "Guard Boi"
"""The author of the package"""

__description__: str = "Useful link managment class"
"""A short description of the package"""

__licence__: str = "MIT"
"""The licence type of the package"""

__version__ = metadata.version("advlink")
"""The version of the package"""

# python3 -m twine upload --repository pypi dist/*