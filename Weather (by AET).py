#mod by Anonumyc Economy Team.

from .. import loader, utils  # pylint: disable=relative-beyond-top-level
import logging
import requests

logger = logging.getLogger(__name__)


def register(cb):
    cb(WWTrMod())


@loader.tds
class WWWTrMod(loader.Module):
    """Погода by wttr.in"""

    strings = {"name": "Погодка"}

    async def client_ready(self, client, db):
        self.client = client

    @loader.sudo
    async def weathercmd(self, message):
        """.w <твой мухосранск>"""
        message.edit("<b>Спиздил погоду с wttr.in</b>")
        city = utils.get_args(message)
        msg = []
        if city:
            await message.edit("Щя узнаем...")
            for i in city:
                r = requests.get(
                    "https://wttr.in/" + i + "?format=%l:+%c+%t,+%w+%m"
                )
                msg.append(r.text)
            await message.edit("".join(msg))
        else:
            await message.edit("Щя узнаем...")
            r = requests.get("https://wttr.in/?format=%l:+%c+%t,+%w+%m")
            await message.edit(r.text)