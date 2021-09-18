#mod by Anonumyc Economy Team.

from .. import loader
from random import choice as какаша


def register(cb):
	cb(ChatinfoMod())

class PickaperMod(loader.Module):
	"""Рандомная фраза пикапа."""
	strings = {'name': 'Пикап Мастер :3'}

	async def pikapcmd(self, event):
		'''Случайная фраза пикапа.'''
		await event.edit('<b>\u2060</b>')
		while True:
			a=какаша(await event.client.get_messages('pikapr',1000))
			if not a.entities:
				await event.edit(f'<b>{a.text}</b>')
				break 
			else:
				pass


		