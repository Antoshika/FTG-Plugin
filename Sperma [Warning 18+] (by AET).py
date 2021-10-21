#mod by Anonumyc Economy Team

from time import sleep
from telethon import events
import asyncio
from.. import loader 

def register(cb):
	cb(SpermaMod()) 
	
class SpermaMod(loader.Module):
	"""Сперма"""
	strings = {'name': 'Магическая сперма! 🍗'} 
	
	async def spermacmd(self, message):
		"""Просто .sperma"""
		for i in range(25):
			a = i + 1
			sleep(0.1)
			await message.edit("Поздравляю, на секторе сперма! В вас запустили МАГИЧЕСКОЙ спермой! " + "💦💦💦👀💦💦💦☁💦💦💦💦💦💦👅💦💦💦💦💦💦💦💦💦💦💦it's cuuuuuuuuuuuuuuuuuuuuuuum Агх~ ахх~ ммм, КАНЧАЮ💦💦.💦эта сперма ПРЕКРАСНА!!!💦.💦ты прекрасен(-а) " + "🎅👸обрызгай всех и всего кого любишь!" +"КООНЧАААА" * a + "...")
