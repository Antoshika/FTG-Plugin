#mod by Anonumyc Economy Team

from .. import loader, utils

import logging

from telethon import functions, types
from telethon.tl.types import PeerUser, PeerChat, PeerChannel, ChannelParticipantsAdmins
logger = logging.getLogger(__name__)


def register(cb):
    cb(TagMod())


@loader.tds
class TagMod(loader.Module):
    """
    Tag :
    -> Тэгнуть всех дадимон (стать крысой, и всё сдать админу).
    -> Тэгнуть всех слитых ботов (Чё эт?).
    -> Тэгнуть всех чебуреков (Не ебу? ?).\n
    кАманды :
     
    """
    strings = {"name": "ТэгальникЖОП",
               "error_chat": "<b>Слушай, как-бы эту команду можно использовать тока в группах и каналах :/.</b>",
               "unknow": ("Ой, чему-то пришла пизда. Шишбки произошла..."
                          "\n\nЭт, напиши в репорт там о проблеме. "
                          "<a href='https://github.com/Antoshika/FTG-Plugin'> Мой Github</a>."),
               "user_link": "\n• <a href='tg://user?id={}'>{}</a>"}

    def config_complete(self):
        self.name = self.strings["name"]

    async def admincmd(self, message):
        """
        .admin : Тэгнуть всех дадимон (кроме слитых ботов).
        .admin [сисимеська] : Тэгнуть всех дадимов (кроме слитых ботов) с поссланием "Н*х*й" ой...
         
        """
        if isinstance(message.to_id, PeerUser):
            await utils.answer(message, self.strings["error_chat"])
            return
        if utils.get_args_raw(message):
            rep = utils.get_args_raw(message)
        else:
            rep = ""
        user = await utils.get_target(message)
        if isinstance(message.to_id, PeerChat) or isinstance(message.to_id, PeerChannel):
            async for user in message.client.iter_participants(message.to_id, filter=ChannelParticipantsAdmins):
                if not user.bot:
                    user_name = user.first_name
                    if user.last_name is not None:
                        user_name += " " + user.last_name
                    rep += self.strings["user_link"].format(user.id, user_name)
            await utils.answer(message, rep)
        else:
            await utils.answer(message, self.strings["unknow"])

    async def allcmd(self, message):
        """
        .all : Тэгнуть всех чебуреков.
        .all [сисимеська] : Тэгнуть всех чебуреков с поссланием "Жопа" ой...
         
        """
        if isinstance(message.to_id, PeerUser):
            await utils.answer(message, self.strings["error_chat"])
            return
        if utils.get_args_raw(message):
            rep = utils.get_args_raw(message)
        else:
            rep = ""
        user = await utils.get_target(message)
        if isinstance(message.to_id, PeerChat) or isinstance(message.to_id, PeerChannel):
            async for user in message.client.iter_participants(message.to_id):
                user_name = user.first_name
                if user.last_name is not None:
                    user_name += " " + user.last_name
                rep += self.strings["user_link"].format(user.id, user_name)
            await utils.answer(message, rep)
        else:
            await utils.answer(message, self.strings["unknow"])

    async def botcmd(self, message):
        """
        .bot : Тэгнуть всех слитых ботов.
        .bot [сисимеська] : Тэгнуть всех слитых ботов с поссланием "вы слитые" ой...
         
        """
        if isinstance(message.to_id, PeerUser):
            await utils.answer(message, self.strings["error_chat"])
            return
        if utils.get_args_raw(message):
            rep = utils.get_args_raw(message)
        else:
            rep = ""
        user = await utils.get_target(message)
        if isinstance(message.to_id, PeerChat) or isinstance(message.to_id, PeerChannel):
            async for user in message.client.iter_participants(message.to_id):
                if user.bot:
                    user_name = user.first_name
                    if user.last_name is not None:
                        user_name += " " + user.last_name
                    rep += self.strings["user_link"].format(user.id, user_name)
            await utils.answer(message, rep)
        else:
            await utils.answer(message, self.strings["unknow"])