#mod by Anonumyc Economy Team.

from .. import loader, utils
import re
from telethon.errors import ChannelInvalidError

@loader.tds
class SenderMod(loader.Module):
    strings = {'name': 'Отправка СМС по чатам'}
    @loader.owner
    async def sndcmd(self, m):
        """.snd <канал/чат/id> <reply>
        Отпрпвить сообшение в чат/канал(без авторства)
        """
        args = utils.get_args_raw(m)
        reply = await m.get_reply_message()
        if not args: return await m.edit("[Почтальён!] Какой адрес канала/чата?")
        try: this = await m.client.get_input_entity(int(args) if re.match(r'-{0,1}\d+', args) else args)
        except ChannelInvalidError as e: return await m.edit("[Почтальён!] Чёт ты мне не тот адрес дал?")
        except Exception as e: return await m.edit("[Почтальён!] Блять, мопед сломался.:\n"+" ".join(e.args))
        ok = await m.client.send_message(this, reply)
        await m.edit("[Почтальён!] Поссылка будет успешно разъёбана!")