#mod by Anonumyc Economy Team.

from .. import loader, utils
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError


def register(cb):
    cb(DeanonMod())
    
class DeanonMod(loader.Module):
    """ДеанОнчик"""
    strings = {'name': 'ДеанОнчик'}

    async def deanoncmd(self, message):
        """Используй: .deanon <Номер телефона и т.д>."""
        chat = "@tapokgod_bot"
        text = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        if not text and not reply:
            await message.edit("<b>Ожидаю номер быдла...🚬</b>")
            return
        await message.edit("<b>Щяс, секундОчку...⌚</b>")
        async with message.client.conversation(chat) as conv:
            if text:
                try:
                    response = conv.wait_event(events.NewMessage(incoming=True, from_users=2051684864))
                    await message.client.send_message(chat, text)
                    response = await response
                except YouBlockedUserError:
                    await message.edit("<b>Разблокируй @tapokgod_bot</b>")
                    return
            else:
                try:
                    user = await utils.get_user(reply)
                    response = conv.wait_event(events.NewMessage(incoming=True, from_users=2051684864))
                    await message.client.send_message(chat, f"{reply.raw_text} (с) {user.first_name}")
                    response = await response
                except YouBlockedUserError:
                    await message.edit("<b>Разблокируй (@tapokgod_bot</b>)")
                    return
            if text:
                try:
                    response = conv.wait_event(events.NewMessage(incoming=True, from_users=2051684864))
                    await message.client.send_message(chat, text)
                    response = await response
                except YouBlockedUserError:
                    await message.edit("<b>Разблокируй (@tapokgod_bot</b>)")
                    return
            else:
                try:
                    user = await utils.get_user(reply)
                    response = conv.wait_event(events.NewMessage(incoming=True, from_users=2051684864))
                    await message.client.send_message(chat, f"{reply.raw_text} (с) {user.first_name}")
                    response = await response
                except YouBlockedUserError:
                    await message.edit("<b>Разблокируй (@tapokgod_bot</b>)")
                    return
            if text:
                try:
                    response = conv.wait_event(events.NewMessage(incoming=True, from_users=2051684864))
                    await message.client.send_message(chat, text)
                    response = await response
                except YouBlockedUserError:
                    await message.edit("<b>Разблокируй (@tapokgod_bot</b>)")
                    return
            else:
                try:
                    user = await utils.get_user(reply)
                    response = conv.wait_event(events.NewMessage(incoming=True, from_users=2051684864))
                    await message.client.send_message(chat, f"{reply.raw_text} (с) {user.first_name}")
                    response = await response
                except YouBlockedUserError:
                    await message.edit("<b>Разблокируй (@tapokgod_bot</b>)")
                    return
        if response.text:
            await message.client.send_message(message.to_id, f"<b> {response.text}</b>")
            await message.delete()
        if response.media:
            await message.client.send_file(message.to_id, response.media, reply_to=reply.id if reply else None)
            await message.delete()