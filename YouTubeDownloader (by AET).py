#mod by Anonumyc Economy Team

"""
Скачиваем Видео и Аудио с помощью YouTube~Downloader
.yta mp3 - аудио.
.ytv mp4 - видео.
"""

import os
import time
import math
import asyncio
from youtube_dl import YoutubeDL
from youtube_dl.utils import (DownloadError, ContentTooShortError,
                              ExtractorError, GeoRestrictedError,
                              MaxDownloadsReached, PostProcessingError,
                              UnavailableVideoError, XAttrMetadataError)
from asyncio import sleep
from telethon.tl.types import DocumentAttributeAudio
from uniborg.util import admin_cmd

async def progress(current, total, event, start, type_of_ps, file_name=None):
    """Общий progress_callback для загрузки и скачивания."""
    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion
        progress_str = "{0}{1} {2}%\n".format(
            ''.join(["▰" for i in range(math.floor(percentage / 10))]),
            ''.join(["▱" for i in range(10 - math.floor(percentage / 10))]),
            round(percentage, 2))
        tmp = progress_str + \
            "{0} of {1}\nETA: {2}".format(
                humanbytes(current),
                humanbytes(total),
                time_formatter(estimated_total_time)
            )
        if file_name:
            await event.edit("{}\nНазвание файлика: `{}`\n{}".format(
                type_of_ps, file_name, tmp))
        else:
            await event.edit("{}\n{}".format(type_of_ps, tmp))


def humanbytes(size):
    """Ввод в байтах,
    вывод в удобный формат для человека. Чтобы всё по красоте было)"""
    # https://stackoverflow.com/a/49361727/4723940
    if not size:
        return ""
    # 2 ** 10 = 1024
    power = 2**10
    raised_to_pow = 0
    dict_power_n = {0: "", 1: "Ki", 2: "Mi", 3: "Gi", 4: "Ti"}
    while size > power:
        size /= power
        raised_to_pow += 1
    return str(round(size, 2)) + " " + dict_power_n[raised_to_pow] + "B"


def time_formatter(milliseconds: int) -> str:
    """Вводятся миллисекунды,
    получаем удобную строку"""
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + " day(s), ") if days else "") + \
        ((str(hours) + " hour(s), ") if hours else "") + \
        ((str(minutes) + " minute(s), ") if minutes else "") + \
        ((str(seconds) + " second(s), ") if seconds else "") + \
        ((str(milliseconds) + " millisecond(s), ") if milliseconds else "")
    return tmp[:-2]

@borg.on(admin_cmd(pattern="yt(a|v) (.*)"))
async def download_video(v_url):
    """ Для команды .ytdl загрузите медиа с YouTube и других сайтов. """
    url = v_url.pattern_match.group(2)
    type = v_url.pattern_match.group(1).lower()

    await v_url.edit("`Начинаю ебальню...`")

    if type == "a":
        opts = {
            'format':
            'bestaudio',
            'addmetadata':
            True,
            'key':
            'FFmpegMetadata',
            'writethumbnail':
            True,
            'prefer_ffmpeg':
            True,
            'geo_bypass':
            True,
            'nocheckcertificate':
            True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            }],
            'outtmpl':
            '%(id)s.mp3',
            'quiet':
            True,
            'logtostderr':
            False
        }
        video = False
        song = True

    elif type == "v":
        opts = {
            'format':
            'best',
            'addmetadata':
            True,
            'key':
            'FFmpegMetadata',
            'prefer_ffmpeg':
            True,
            'geo_bypass':
            True,
            'nocheckcertificate':
            True,
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4'
            }],
            'outtmpl':
            '%(id)s.mp4',
            'logtostderr':
            False,
            'quiet':
            True
        }
        song = False
        video = True

    try:
        await v_url.edit("`Идёт подгрузка данных в фбр, жди...`")
        with YoutubeDL(opts) as ytdl:
            ytdl_data = ytdl.extract_info(url)
    except DownloadError as DE:
        await v_url.edit(f"`{str(DE)}`")
        return
    except ContentTooShortError:
        await v_url.edit("`Слушай, я понимаю у тебя короткий. Ну почему видео такое короткое?...`")
        return
    except GeoRestrictedError:
        await v_url.edit(
            "`Слухай, чёт видос недоступен в твоем городке. Шо, Full/XXX хотел скачать? А не, не получилось :D`"
        )
        return
    except MaxDownloadsReached:
        await v_url.edit("`Лимит насилование на приделе.`")
        return
    except PostProcessingError:
        await v_url.edit("`Чёт, проблемка какая-то. Чёт ты сломал...`")
        return
    except UnavailableVideoError:
        await v_url.edit("`В данном форматике медиа для тебя недоступно.`")
        return
    except XAttrMetadataError as XAME:
        await v_url.edit(f"`{XAME.code}: {XAME.msg}\n{XAME.reason}`")
        return
    except ExtractorError:
        await v_url.edit("`Произошла ШИШИБКА при вытаскивание инфы...`")
        return
    except Exception as e:
        await v_url.edit(f"{str(type(e)): {str(e)}}")
        return
    c_time = time.time()
    if song:
        await v_url.edit(f"`Начинаю качать 666гб шарманки...:`\
        \n**{ytdl_data['title']}**\
        \nby *{ytdl_data['uploader']}*")
        await v_url.client.send_file(
            v_url.chat_id,
            f"{ytdl_data['id']}.mp3",
            supports_streaming=True,
            attributes=[
                DocumentAttributeAudio(duration=int(ytdl_data['duration']),
                                       title=str(ytdl_data['title']),
                                       performer=str(ytdl_data['uploader']))
            ],
            progress_callback=lambda d, t: asyncio.get_event_loop(
            ).create_task(
                progress(d, t, v_url, c_time, "Щя, загружу в кэш...:",
                         f"{ytdl_data['title']}.mp3")))
        os.remove(f"{ytdl_data['id']}.mp3")
        await v_url.delete()
    elif video:
        await v_url.edit(f"`Начинаю качать XXX видос...:`\
        \n**{ytdl_data['title']}**\
        \nby *{ytdl_data['uploader']}*")
        await v_url.client.send_file(
            v_url.chat_id,
            f"{ytdl_data['id']}.mp4",
            supports_streaming=True,
            caption=ytdl_data['title'],
            progress_callback=lambda d, t: asyncio.get_event_loop(
            ).create_task(
                progress(d, t, v_url, c_time, "Щя, загружу в кэш...:",
                         f"{ytdl_data['title']}.mp4")))
        os.remove(f"{ytdl_data['id']}.mp4")
        await v_url.delete()