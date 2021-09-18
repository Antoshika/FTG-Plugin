# created -> Anonumyc Economy Team.

from pydub import AudioSegment 
from .. import loader, utils 
from telethon import types 
import io 
def register(cb): 
 cb(AudioConverterMod()) 
class AudioConverterMod(loader.Module): 
 """Конвертер музыкальных файлов, в разные форматы.""" 
 strings = {'name': 'AudioConverter'} 
 def __init__(self): 
  self.name = self.strings['name'] 
  self._me = None 
  self._ratelimit = [] 
 async def client_ready(self, client, db): 
  self._db = db 
  self._client = client 
  self.me = await client.get_me() 
 async def tovoicecmd(self, message): 
  """.tovoice <гдэ аудио?> 
      Сделать музыку в войс.
  """ 
  reply = await message.get_reply_message() 
  if not reply: 
   await message.edit("А гдэ файл?!") 
   return 
  else: 
   try: 
    if reply.media.document.attributes[0].voice == True: 
     await message.edit("Придурок, это войс, а не аудиофайл!") 
     return 
   except: 
    await message.edit("Придурок, это не аудиофайл!") 
    return 
  await message.edit("[LALALALAL] СкачиваемКа...") 
  au = io.BytesIO() 
  await message.client.download_media(reply.media.document, au) 
  au.seek(0) 
  await message.edit("[LALALALAL] Создаём голосовуху...") 
  audio = AudioSegment.from_file(au) 
  m = io.BytesIO() 
  m.name="voice.ogg"  
  audio.split_to_mono() 
  await message.edit("[[LALALALAL] Пиздим...") 
  dur = len(audio)/1000 
  audio.export(m, format="ogg", bitrate="64k", codec="libopus") 
  await message.edit("[LALALALAL] Высылаем по почте...") 
  m.seek(0) 
  await message.client.send_file(message.to_id, m, reply_to=reply.id, voice_note=True, duration=dur) 
  await message.delete() 
 async def toformatcmd(self, message): 
  """.toformat [format] <reply to audio> 
      Сконвертировать аудио/видео/войс в нужный формат 
   Поддерживаются mp3, m4a, ogg, mpeg, wav, oga 
  """ 
  frmts = ['ogg', 'mpeg', 'mp3', 'wav', 'oga', 'm4a', '3gp'] 
  reply = await message.get_reply_message() 
  if not reply: 
   await message.edit("А гдэ файл?!") 
   return 
  else: 
   try: 
    reply.media.document.attributes[0].duration 
    if utils.get_args_raw(message): 
     if utils.get_args_raw(message) not in frmts: 
      await message.edit(f"Формат {utils.get_args_raw(message)} для харчевни не поддерживается!") 
      return 
     formatik = utils.get_args_raw(message) 
    else: 
     await message.edit("Какой надо те форматик?") 
     return 
   except: 
    await message.edit("Придурок, это не аудиофайл!") 
    return 
  await message.edit("[LALALALAL] СкачиваемКа....") 
  au = io.BytesIO() 
  await message.client.download_media(reply.media.document, au) 
  au.seek(0) 
  await message.edit(f"[AudioConverter] Харкнули в {formatik}...") 
  audio = AudioSegment.from_file(au) 
  m = io.BytesIO() 
  m.name="Converted_to." + formatik 
  audio.split_to_mono() 
  await message.edit("[[LALALALAL] Пиздим...") 
  audio.export(m, format=formatik) 
  await message.edit("[LALALALAL] Высылаем по почте...") 
  m.seek(0) 
  await message.client.send_file(message.to_id, m, reply_to=reply.id, attributes=[types.DocumentAttributeAudio(duration = reply.document.attributes[0].duration, title=f"Converted to " + formatik, performer="Anonumec ET.")]) 
  await message.delete()