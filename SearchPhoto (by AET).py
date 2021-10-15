#mod by Anonumyc Economy Team
import logging

from .. import loader, utils

logger = logging.getLogger(__name__)


class GetPPMod(loader.Module):
    """Description for module"""
    strings = {"name": "Поиск Фото"}

    async def client_ready(self, client, db):
        self.client = client
        self.db = db

    async def potocmd(self, message):
        """Выкидывает фотоОчки"""
        id = utils.get_args_raw(message)
        user = await message.get_reply_message()
        chat = message.input_chat
        if user:
            photos = await self.client.get_profile_photos(user.sender)
            u = True
        else:
            photos = await self.client.get_profile_photos(chat)
            u = False
        if id.strip() == "":
            if len(photos) > 0:
                await self.client.send_file(message.chat_id, photos)
            else:
                try:
                    if u is True:
                        photo = await self.client.download_profile_photo(user.sender)
                    else:
                        photo = await self.client.download_profile_photo(message.input_chat)
                    await self.client.send_file(message.chat_id, photo)
                except:
                    await message.edit("<code>Он какой-то лох, у него нету фоток.</code>")
                    return
        else:
            try:
                id = int(id)
                if id <= 0:
                    await message.edit("<code>Написанный вами ID-шник бомжа не найден. </code>")
                    return
            except:
                 await message.edit("<code>ID is invalid</code>")
                 return
            if int(id) <= (len(photos)):
                send_photos = await self.client.download_media(photos[id - 1])
                await self.client.send_file(message.chat_id, send_photos)
            else:
                await message.edit("<code>ФотОчка с таким именем не найдено :\</code>")
                return