#mod by Anonumyc Economy Team

import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from uniborg.util import admin_cmd
@borg.on(admin_cmd("story ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("```Дядь, дай реплей на СМС-ку человечка!```")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.text:
       await event.edit("```аоаоао, а ты пробывал(-а) ввести команду правильно? 🗿```")
       return
    chat = "@HistoryAIBot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit("```АЛЛОООО, ОТВЕТЬ НА СООБЩЕНИЕ REAL ЧЕЛА! 🕶```")
       return
    await event.edit("```Щя погодь, работаю... ✨```")
    await event.delete()
    async with borg.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1045054453))
              await borg.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```Эу, попробуй включить @HistoryAIBot и повторить```")
              return
          if response.text.startswith("Салам алейкум, я дополню твою хуйню при помощи НЕЙРОСИТИ!!."):
             await event.edit("```Слухай, отключил пункт в конфиденциальности пересылки.```")
          else: 
             await borg.forward_messages(event.chat_id, response.message)