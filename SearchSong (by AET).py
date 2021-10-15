#mod by Anonumyc Economy Team

from .. import loader, utils 
 
@loader.tds 
class SearchMusicMod(loader.Module): 
    """ 
    Модуль SearchMusic - поиск вашей разнос ушей 
    """ 
    strings = {"name": "ПоискШарманки"} 
 
    async def smcmd(self, message): 
        """Введите команду: .sm :"название" чтобы найти шарману по названию.""" 
        args = utils.get_args_raw(message) 
        reply = await message.get_reply_message() 
        if not args: 
            return await message.edit("<b>А что блять мне искать?.</b>")  
        try: 
            await message.edit("<b>Щя погодь, ищу...</b>") 
            music = await message.client.inline_query('lybot', args) 
            await message.delete() 
            await message.client.send_file(message.to_id, music[0].result.document, reply_to=reply.id if reply else None) 
        except: return await message.client.send_message(message.chat_id, f"<b>Шарманка с именем <code>{args}</code> потерялась :C.</b>")