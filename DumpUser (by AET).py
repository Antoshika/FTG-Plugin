#mod by Anonumyc Economy Team

from .. import loader, utils
import os
def register(cb):
	cb(DUsersMod())
class DUsersMod(loader.Module):
	"""DUsers"""
	strings = {'name': 'Дамп~User'}
	def __init__(self):
		self.name = self.strings['name']
		self._me = None
		self._ratelimit = []
	async def client_ready(self, client, db):
		self._db = db
		self._client = client
		self.me = await client.get_me()
	async def ducmd(self, message):
		""".du <n> <m> <s>
		    Дамп~User'ов мусорки.
			<num> - Получить только чебурков дебилов с открытыми номерками.
			<m> - Отправить дамп в эту мусорку.
			<silent> - Тихий и незаметный дамп...
		"""
		num = False
		silent = False
		tome = False
		if(utils.get_args_raw(message)):
			a = utils.get_args_raw(message)
			if("n" in a):
				num = True
			if("s" in a):
				silent = True
			if("m" in a):
				tome = True
		if silent == False:
			await message.edit("🍕 Дамп-дамп-дампим чат... 🍕")
		else:
			await message.delete()
		f = open(f"dump-{str(message.to_id)}.txt", "w")
		f.write("FNAME;LNAME;USER;ID;NUMBER\n")
		me = await message.client.get_me()
		for i in await message.client.get_participants(message.to_id):
			if(i.id == self.me.id): continue
			if(num):
				if(i.phone):
					f.write(f"{str(i.first_name)};{str(i.last_name)};{str(i.username)};{str(i.id)};{str(i.phone)}\n")
			else:
				f.write(f"{str(i.first_name)};{str(i.last_name)};{str(i.username)};{str(i.id)};{str(i.phone)}\n")
		f.close()
		if tome:
			await message.client.send_file('me', f"dump-{str(message.to_id)}.txt", caption="Дамп мусорки " + str(message.to_id))
		else:
			await message.client.send_file(message.to_id, f"dump-{str(message.to_id)}.txt", caption="Дамп мусорки " + str(message.to_id))
		if silent == False:
			if tome:
				if num:
					await message.edit("🖤Дамп~User'ов мусорки был сохранён в сохранёнки!🖤")
				else:
					await message.edit("🖤Дамп~User'ов мусорки с открытыми номерками был сохранён в сохранёнки!🖤")
			else:
				await message.delete()