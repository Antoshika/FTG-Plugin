#mod by Anonumyc Economy Team.

from .. import loader
from telethon.tl.types import *
@loader.tds
class InformationMod(loader.Module):
  "Статистика чата"
  strings = {"name": "Статистика мусорки"}
  @loader.owner
  async def statacmd(self, m):
	  await m.edit("<b>📊Щя посмотрим...</b>")
	  al = str((await m.client.get_messages(m.to_id, limit=0)).total)
	  ph = str((await m.client.get_messages(m.to_id, limit=0, filter=InputMessagesFilterPhotos())).total)
	  vi = str((await m.client.get_messages(m.to_id, limit=0, filter=InputMessagesFilterVideo())).total)
	  mu = str((await m.client.get_messages(m.to_id, limit=0, filter=InputMessagesFilterMusic())).total)
	  vo = str((await m.client.get_messages(m.to_id, limit=0, filter=InputMessagesFilterVideo())).total)
	  vv = str((await m.client.get_messages(m.to_id, limit=0, filter=InputMessagesFilterRoundVideo())).total)
	  do = str((await m.client.get_messages(m.to_id, limit=0, filter=InputMessagesFilterDocument())).total)
	  urls = str((await m.client.get_messages(m.to_id, limit=0, filter=InputMessagesFilterUrl())).total)
	  gifs = str((await m.client.get_messages(m.to_id, limit=0, filter=InputMessagesFilterGif())).total)
	  geos = str((await m.client.get_messages(m.to_id, limit=0, filter=InputMessagesFilterGeo())).total)
	  cont = str((await m.client.get_messages(m.to_id, limit=0, filter=InputMessagesFilterContacts())).total)
	  await m.edit(
	    ("<b>✉️Всего матов:</b> {}\n"+
	    "<b>🖼️Всего фуллов:</b> {}\n"+
	    "<b>📹Всего фистингов:</b> {}\n"+
	    "<b>🎵Всего разлом ушей: :</b> {}\n"+
	    "<b>🎶Всего писков:</b> {}\n"+
	    "<b>🎥Всего фистингов(круглых):</b> {}\n"+
	    "<b>📂Всего хаков:</b> {}\n"+
	    "<b>🔗Всего хентаев:</b> {}\n"+
	    "<b>🎞️Всего GIF:</b> {}\n"+
	    "<b>🗺️Всего отправленных координат:</b> {}\n"+
	    "<b>👭Контаков:</b> {}").format(al, ph, vi, mu, vo, vv, do, urls, gifs, geos, cont))