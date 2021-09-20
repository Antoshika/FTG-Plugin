#mod by Anonumyc Economy Team.

from .. import loader, utils

@loader.tds
class GroupTagMod(loader.Module):
    """Тегает определенные \"группы\""""
    strings = {'name': 'Бог Групп'}

    async def client_ready(self, client, db):
        self.db = db

    async def addgroupcmd(self, message):
        """Добавить группу: .addgroup <название>."""
        groups = self.db.get("GroupTag", "groups", {})
        args = utils.get_args_raw(message)

        if not args:
            return await message.edit("Гадэ Аргументы?!")

        if args not in groups:
            groups.setdefault(args, [])
            self.db.set("GroupTag", "groups", groups)
            return await message.edit(f"Мусорка {args} добавлена!")
        else:
            return await message.edit("Мусорка с таким прозвищем уже есть!")


    async def delgroupcmd(self, message):
        """Удалить группу: .delgroup <название>."""
        groups = self.db.get("GroupTag", "groups", {})
        args = utils.get_args_raw(message)

        if not args:
            return await message.edit("Гадэ Аргументы?!")

        if args in groups:
            groups.pop(args)
            self.db.set("GroupTag", "groups", groups)
            return await message.edit(f"Мусорка {args} удалена!")
        else:
            return await message.edit("Мусорка с таким прозвищем нету!")


    async def grusertagcmd(self, message):
        """Добавить/удалить пользователя в группу: .grusertag <@ или реплай>."""
        groups = self.db.get("GroupTag", "groups", {})
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()

        if not args and not reply:
            return await message.edit("Гадэ Аргументы?!")
        args = args.split()

        try:
            if reply:
                args = utils.get_args_raw(message)
                if args:
                    group = args
                    if group not in groups:
                        return await message.edit("Такой мусорки нема!")
                else:
                    return await message.edit("Гадэ Аргументы?!")

                user = await message.client.get_entity(reply.sender_id)
            else:
                user = await message.client.get_entity(args[1] if not args[1].isnumeric() else int(args[1]))
                if len(args) == 1:
                    return await message.edit("Мало аргументов!")
                elif len(args) >= 2:
                    group = args[0]
        except (IndexError, ValueError):
            return await message.edit("Неверно указал осёл аргументы.\nВообще-то правильно: <code>.addusertag <мусорка> <@ или реплай></code>.")
        else:
            if user.id in groups[group]:
                groups[group].remove(user.id)
                await message.edit(f"{user.first_name} был удален из мусорки! {group}!")
            else:
                groups[group].append(user.id)
                await message.edit(f"{user.first_name} был добавлен в мусорку! {group}!")
            return self.db.set("GroupTag", "groups", groups)


    async def groupcmd(self, message):
        """Вывести список групп, или показать участников группы: .group <группа>; ничего."""
        groups = self.db.get("GroupTag", "groups", {})
        args = utils.get_args_raw(message)

        if args:
            if args not in groups:
                return await message.edit("Такой мусорки нема!")

            msg = ""
            for _ in groups[args]:
                user = await message.client.get_entity(_)
                msg += f"• {user.first_name} (<code>{_}</code>)\n"

            return await message.edit(f"Список Абобусов в мусорки {args}:\n\n{msg}")

        if len(groups) == 0:
            return await message.edit("Пока что еще нет мусорок!")

        msg = ""
        for _ in groups:
            msg += f"• {_}\n"

        return await message.edit(f"Список мусорок для тЭга:\n\n{msg}")


    async def grouptagcmd(self, message):
        """Начать тегать всех в группе: .grouptag <группа> <текст>; ничего."""
        groups = self.db.get("GroupTag", "groups", {})
        args = utils.get_args_raw(message)
        tag = None

        if not args:
            return await message.edit("Гадэ Аргументы?!")

        argss = args.split()
        if argss[0] not in groups:
            return await message.edit("Такой мусорки нема!")

        group = argss[0]
        if len(argss) == 1:
            tag = "говно залупное\n                пашет."
        elif len(argss) >= 2:
            tag = args.split(' ', 1)[1]

        notifies = []
        for userid in groups[group]:
            notifies.append(f"<a href='tg://user?id={userid}'>\u2060</a>")
        chunkss = list(chunks(notifies, 5))
        await message.delete()
        for chunk in chunkss:
            await message.client.send_message(message.to_id, tag + '\u2060'.join(chunk))


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]