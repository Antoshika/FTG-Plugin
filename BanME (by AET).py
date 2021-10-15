#mod by Anonumyc Economy Team

from .. import loader, utils
from asyncio import sleep
from telethon.tl.functions.channels import LeaveChannelRequest
@loader.tds
class LeaveMod(loader.Module):
	strings = {"name": "Ёбни меня"}
	@loader.sudo
	async def banmecmd(self, message):
		""".banme"""
		if not message.chat:
			await message.edit("<b>Ты успешно ебанул бутылкой себя, больше ты не сможешь вернуться за пивом...</b>")
			return
		text = utils.get_args_raw(message)
		if not text:
			text = "Ты успешно ебанул бутылкой себя, больше ты не сможешь вернуться за пивом..."
		if text.lower() == "del":
			await message.delete()
		else:
			await message.edit(f"<b>{text}</b>")
		await sleep(10)
		await message.client(LeaveChannelRequest(message.chat_id))
		