#mod by Anonumyc Economy Team.

from telethon import events
from telethon import functions
import asyncio
from telethon import errors
from .. import loader, utils

class addmembersMod(loader.Module):

    strings = {"name":"КикВсех & ДобавитьВсех"}

    async def adduserscmd(self, event):
        """Добавляет людей с чата в чат."""
        if len(event.text.split()) == 2:
            idschannelgroup = event.text.split(" ", maxsplit=1)[1]
            user = [i async for i in event.client.iter_participants(event.to_id.channel_id)]
            await event.edit(f"<b>{len(user)} бомжей будет приглашено из мусорки {event.to_id.channel_id} в другую мусорку {idschannelgroup}</b>")
            for u in user:
                try:
                    try:
                        if u.bot == False:
                            await event.client(functions.channels.InviteToChannelRequest(idschannelgroup, [u.id]))
                            await asyncio.sleep(1)
                        else:
                            pass
                    except:
                        pass
                except errors.FloodWaitError as e:
                    print('Flood for', e.seconds)
        else:
            await event.edit(f"<b>Куда их будем отправлять?</b>")
    
    async def kickallcmd(self, event):
        """Удаляет всех пользователей из чата."""
        user = [i async for i in event.client.iter_participants(event.to_id.channel_id)]
        await event.edit(f"<b>{len(user)} бомжей будет кикнуто из мусорки {event.to_id.channel_id}</b>")
        for u in user:
            try:
                try:
                    if u.is_self != True:
                        await event.client.kick_participant(event.chat_id, u.id)
                        await asyncio.sleep(1)
                    else:
                        pass
                except:
                    pass
            except errors.FloodWaitError as e:
                print('Flood for', e.seconds)