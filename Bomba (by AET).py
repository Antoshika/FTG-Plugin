#mod by Anonumyc Economy Team

from telethon import events
import asyncio
import os
import sys


@borg.on(events.NewMessage(pattern=r"\.bombs", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
       
 
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await event.edit("💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await event.edit("▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n")
    await asyncio.sleep(1)
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💥💥💥💥 \n")
    await asyncio.sleep(0.5)
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💥💥💥💥 \n💥💥💥💥 \n")
    await asyncio.sleep(0.5)
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n😵😵😵😵 \n")
    await asyncio.sleep(0.5)
    await event.edit("БУХ ЕБАТЬ! ТВОЮ ЖОПУ ВЗОРВОЛО! TERRORIST WIN")