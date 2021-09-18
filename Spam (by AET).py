#mod by Anonumyc Economy Team.

from .. import loader, utils
from asyncio import sleep
@loader.tds
class spamMod(loader.Module):
	strings = {"name": "Спам АТАКА!"}
	@loader.owner
	async def spamcmd(self, message):
		'''.spam {задержка} {повтор} {текст}'''
		text = utils.get_args_raw(message)
		try:
			num = float(text.split(' ')[0])
		except ValueError:
			await message.edit('<strong>Еблан, задержку правильно напиши!.</strong>')
			return
		try:
			num1 = int(text.split(' ')[1])
		except ValueError:
			await message.edit('<strong>Еблан, повтор правильно напиши!.</strong>')
			return
		text=text.split(' ',maxsplit=2)[2]
		await message.delete()
		for _ in range(num1):
			await message.client.send_message(message.to_id,text)
			await sleep(num)
			