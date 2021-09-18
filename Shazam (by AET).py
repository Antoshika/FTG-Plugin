#mod by Anonumyc Economy Team.
from ShazamAPI import Shazam
import io
from .. import loader, utils


@loader.tds
class ShazamMod(loader.Module):
    """Shazam API"""
    strings = {'name': 'ШАЗАМ!'}
    tag = "<b>[Shazam]</b> "

    @loader.owner
    async def shazamcmd(self, m):
        '''.shazam <дай хардбасс> - найти трек'''
        s = await get_audio_shazam(m)
        if not s:
            return
        try:
            shazam = Shazam(s.track.read())
            recog = shazam.recognizeSong()
            track = next(recog)[1]['track']
            await m.client.send_file(m.to_id, file=track['images']['background'], caption=self.tag+"Распознанный трек: "+track['share']['subject'], reply_to=s.reply.id)
            await m.delete()
        except:
            await m.edit(self.tag+"Хер тебе, не смог найти...")

    async def shazamtextcmd(self, m):
        '''.shazamtext <дай хардбасс> - узнать текст трека'''
        s = await get_audio_shazam(m)
        if not s:
            return
        try:
            shazam = Shazam(s.track.read())
            recog = shazam.recognizeSong()
            track = next(recog)[1]['track']
            text = track['sections'][1]['text']
            await utils.answer(m, "\n".join(self.tag+f"Текст трека {track['share']['subject']}\n\n"+text))
        except:
            await m.edit(self.tag+"Хер тебе, не смог найти... | Текста нет...")


async def get_audio_shazam(m):
    class rct():
        track = io.BytesIO()
        reply = None
    reply = await m.get_reply_message()
    if reply and reply.file and reply.file.mime_type.split("/")[0] == "audio":
        ae = rct()
        await utils.answer(m, "<b>[Shazam]</b> Скачиваюка...")
        ae.track = io.BytesIO(await reply.download_media(bytes))
        ae.reply = reply
        await m.edit("<b>[Shazam]</b> Бьюсь об стол...")
        return ae
    else:
        await utils.answer(m, "<b>[Shazam]</b> поддерживается только аудиосообщения и мп3.")
        return None