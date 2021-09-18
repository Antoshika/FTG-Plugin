#mod by Anonumyc Economy Team.

from requests.api import request
from .. import loader, utils
from requests import get


@loader.tds
class FullApiMod(loader.Module):
    """Фулл"""
    strings = {'name': 'Фулл!'}

    @loader.owner
    async def rndfullcmd(self, m):
        """.rndfull - получить рандомный фулл :)
        """
        await m.edit("<a href=\""+get("https://api.d4n13l3k00.ru/random_full").json()['url']+"\">Я всегда нахожу фулл❤</a>")