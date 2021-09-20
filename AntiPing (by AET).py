#mod by Anonumyc Economy Team.

from .. import loader, utils
from telethon.tl.types import ChatBannedRights
from telethon.tl.functions.channels import EditBannedRequest


@loader.tds
class AntiMentionMod(loader.Module):
    """Режим AntiMention."""
    strings = {'name': 'Анти.Упоминание'}

    async def client_ready(self, client, db):
        self.db = db

    async def antimentioncmd(self, message):
        """Включить/выключить режим AntiMention. Использование: .antimention <clearall* (по желанию)>.\n* - выключает режим во всех чатах."""
        am = self.db.get("AntiMention", "am", [])
        ac = self.db.get("AntiMention", "action", {})
        args = utils.get_args_raw(message)
        if args == "clearall":
            self.db.set("AntiMention", "am", [])
            self.db.set("AntiMention", "action", {})
            return await message.edit("<b>[Анти-Хуй]</b> Антивирус активирован везде!.")
        if not message.is_private:
            chat = await message.get_chat() 
            if not chat.admin_rights and not chat.creator:
                return await message.edit("<b>Дядел, я не Админус!</b>")
            else:
                if chat.admin_rights.delete_messages == False:
                    return await message.edit("<b>У меня права купленные, а таких нету :C</b>") 
            chatid = str(message.chat_id)
            if chatid in am:
                am.remove(chatid)
                ac.pop(chatid)
                self.db.set("AntiMention", "am", am)
                self.db.set("AntiMention", "action", ac)
                return await message.edit("<b>[Анти-Хуй]</b> Антивирус деактивирован в этом чате.")

            am.append(chatid)
            ac.setdefault(chatid, {})
            ac[chatid].setdefault("action", "none")
            ac[chatid].setdefault("exceptions", [])
            self.db.set("AntiMention", "action", ac)
            self.db.set("AntiMention", "am", am)
            return await message.edit("<b>[Анти-Хуй]</b> Антивирус активирован в этом чате.")
        else: return await message.edit("<b>[Анти-Хуй]</b> Осёл, это не чат!")

    async def amexcmd(self, message):
        """Добавить исключения/посмотреть список исключений. Используй: .amex <@ или реплай> или <clear>."""
        if not message.is_private:
            am = self.db.get("AntiMention", "am", [])
            ac = self.db.get("AntiMention", "action", {})
            chatid = str(message.chat_id)
            args = utils.get_args_raw(message)
            reply = await message.get_reply_message()
            if chatid not in am: return await message.edit("<b>[Анти-Хуй]</b> Антивирус в этом чате, режим деактивирован.")
            if not args and not reply:
                ls = ac[chatid]["exceptions"] 
                users = ""
                for _ in ls:
                    user = await message.client.get_entity(int(_))
                    users += f"• <a href=\"tg://user?id={int(_)}\">{user.first_name}</a> | <b>[</b><code>{_}</code><b>]</b>\n"
                return await message.edit(f"<b>Исключения в этом чате: {len(ls)}</b>\n\n{users}")
            if args == "clear":
                ac[chatid].pop("exceptions") 
                self.db.set("AntiMention", "action", ac)
                return await message.edit(f"<b>[Анти-Хуй]</b> Список ебанутых в этом чате очищен.")
            try:
                if args: user = await message.client.get_entity(int(args) if args.isnumeric() else args)
                else: user = await message.client.get_entity(reply.sender_id)
            except ValueError: await message.edit("<b>Не смог найти бомжа?.</b>")
            userid = str(user.id)
            if userid not in ac[chatid]["exceptions"]:
                ac[chatid]["exceptions"].append(userid) 
                self.db.set("AntiMention", "action", ac)
                return await message.edit(f"<b>[Анти-Хуй]</b> {user.first_name} добавил в список тетради смерти.")
            ac[chatid]["exceptions"].remove(userid) 
            self.db.set("AntiMention", "action", ac)
            return await message.edit(f"<b>[Анти-Хуй]</b> {user.first_name} удалён из списка тетради смерти.")
        else: return await message.edit("<b>[Анти-Хуй]</b> Осёл, это не чат!")

    async def setsamcmd(self, message):
        """Настройки режима AntiMention. Используй: .setsam <режим (kick/ban/mute/none)>; ничего."""
        if not message.is_private:
            am = self.db.get("AntiMention", "am", [])
            ac = self.db.get("AntiMention", "action", {})
            chatid = str(message.chat_id)
            args = utils.get_args_raw(message)
            if chatid in am:
                if args:
                    if args == "kick":
                        ac[chatid].update({"action": "kick"})
                    elif args == "ban":
                        ac[chatid].update({"action": "ban"})
                    elif args == "mute":
                        ac[chatid].update({"action": "mute"})
                    elif args == "none":
                        ac[chatid].update({"action": "none"}) 
                    else: return await message.edit("<b>[Анти-Хуй - НастройОчки]</b> Осёл, такого мода нет в списке.\nЕсть тока такие режимы: kick/ban/mute/нечего.")
                    self.db.set("AntiMention", "action", ac)
                    return await message.edit(f"<b>[Анти-Хуй - НастройОчки]</b> При упоминании я буду вас убивать: {ac[chatid]['action']}.")
                else: return await message.edit(f"<b>[Анти-Хуй - НастройОчки] </b> НастройОчки чатика:\n\n:"
                                                f"<b>Трезвость режима:</b> True\n"
                                                f"<b>При упоминании я буду вас убивать:</b> {ac[chatid]['action']}\n")
            else: return await message.edit("<b>[Анти-Хуй - НастройОчки]</b> Антивирус деактивирован в этом чате..")
        else: return await message.edit("<b>[Анти-Хуй]</b> Осёл, это не чат!")

    async def watcher(self, message):
        """Продам модуль!!"""
        try:
            am = self.db.get("AntiMention", "am", [])
            ac = self.db.get("AntiMention", "action", {})
            chatid = str(message.chat_id)
            if chatid not in am: return
            if message.mentioned:
                userid = message.sender_id
                if str(userid) not in ac[chatid]["exceptions"]:
                    try:
                        if ac[chatid]["action"] == "kick":
                            await message.client.kick_participant(int(chatid), userid)
                        elif ac[chatid]["action"] == "ban":
                            await message.client(EditBannedRequest(int(chatid), userid, ChatBannedRights(until_date=None, view_messages=True)))
                        elif ac[chatid]["action"] == "mute":
                            await message.client(EditBannedRequest(int(chatid), userid, ChatBannedRights(until_date=True, send_messages=True))) 
                        else: pass
                    except: pass 
                    await message.client.delete_messages(int(chatid), message.id)
        except: pass