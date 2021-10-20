#mod by Anonumyc Economy Team

""" 
кАманды:

.geta <ID-Каннала> [загрузит все медиафайла из канала, но есть предел в 3000 из-за ограничений API.]
.getc <Кол-во сообщений и ID-Каннла>  """

 
from telethon import events
import asyncio
import os
import subprocess
import sys
from uniborg.util import admin_cmd, humanbytes, progress, time_formatter

@borg.on(events.NewMessage(pattern=r"\.getc", outgoing=True))
async def get_media(event):
    if event.fwd_from:
        return
    dir= "./temp/"
    try:
        os.makedirs("./temp/")
    except:
    	pass
    channel_username= event.text
    command = ['ls','temp','|','wc','-l' ]
    limit = channel_username[6:9]
    print(limit)
    channel_username = channel_username[11: ]
    print(channel_username)
    await event.edit("Загружаю много чего из этого канала.")
    msgs = await borg.get_messages(channel_username, limit=int(limit))
    with open('log.txt','w') as f:
    	f.write(str(msgs))
    for msg in msgs:
       if msg.media is not None:
	        await borg.download_media(
                msg,dir)
    ps = subprocess.Popen(('ls', 'temp'), stdout=subprocess.PIPE)
    output = subprocess.check_output(('wc', '-l'), stdin=ps.stdout)
    ps.wait()
    output = str(output)
    output = output.replace("b'","")
    output = output.replace("\n'","")
    await event.edit("Загружено "+output+" файлов.")
             
             
             
             
             
             
@borg.on(events.NewMessage(pattern=r"\.geta", outgoing=True))
async def get_media(event):
    if event.fwd_from:
        return
    dir= "./temp/"
    try:
        os.makedirs("./temp/")
    except:
    	pass
    channel_username= event.text
    command = ['ls','temp','|','wc','-l' ]
    channel_username = channel_username[7:]
 
   
    print(channel_username)
    await event.edit("Загружаю ВСЁиз канала.")
    msgs = await borg.get_messages(channel_username,limit=3000)
    with open('log.txt','w') as f:
    	f.write(str(msgs))
    for msg in msgs:
       if msg.media is not None:
	        await borg.download_media(
                msg,dir)          
    ps = subprocess.Popen(('ls', 'temp'), stdout=subprocess.PIPE)
    output = subprocess.check_output(('wc', '-l'), stdin=ps.stdout)
    ps.wait()
    output = str(output)
    output = output.replace("b'","")
    output = output.replace("\n'","")
    await event.edit("Скачено "+output+" файликов.")