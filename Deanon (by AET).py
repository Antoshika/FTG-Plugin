#mod by Anonumyc Economy Team.

from .. import loader, utils
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError


def register(cb):
    cb(NedoQuotesMod())
    
class NedoQuotesMod(loader.Module):
    """Деанонер сделали Anonumyc Economy Team."""
    strings = {'name': 'Деанончик'}

    async def dncmd(self, message):
        """Используй: .dn <Телефончик, обезательно с +>."""
        chat = "@stoned_eyes_bot"
        text = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        if not text and not reply:
            await message.edit("<b>Ожидаю номер быдла...</b>")
            return
        await message.edit("<b>Щя, погоди...</b>")
        async with message.client.conversation(chat) as conv:
            if text:
                try:
                    response = conv.wait_event(events.NewMessage(incoming=True, from_users=1832467332))
                    await message.client.send_message(chat, text)
                    response = await response
                except YouBlockedUserError:
                    await message.edit("<b>Разблокируй (@stoned_eyes_bot</b>)")
                    return
            else:
                try:
                    user = await utils.get_user(reply)
                    response = conv.wait_event(events.NewMessage(incoming=True, from_users=1832467332))
                    await message.client.send_message(chat, f"{reply.raw_text} (с) {user.first_name}")
                    response = await response
                except YouBlockedUserError:
                    await message.edit("<b>Разблокируй (@stoned_eyes_bot</b>)")
                    return
        if response.text:
            await message.client.send_message(message.to_id, f"<b> {response.text}</b>")
            await message.delete()
        if response.media:
            await message.client.send_file(message.to_id, response.media, reply_to=reply.id if reply else None)
            await message.delete()