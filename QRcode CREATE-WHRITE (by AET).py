#mod by Anonumyc Economy Team

"""Создаем или Распозноём QRCode
WARNING! Обязательно пропишите (.terminal pip3 install qrcode)

Команды:

.getqr расшифровка
.makeqr <ваша мазня>"""
from telethon import events
import asyncio
from datetime import datetime
import os
from uniborg.util import admin_cmd
import qrcode
from bs4 import BeautifulSoup

# requires: bs4
# requires: qrcode
 
 
def progress(current, total):
    logger.info("Загрузил {} из {}\nВыполнил {}".format(current, total, (current / total) * 100))
 
 
@borg.on(admin_cmd("getqr"))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    downloaded_file_name = await borg.download_media(
        await event.get_reply_message(),
        Config.TMP_DOWNLOAD_DIRECTORY,
        progress_callback=progress
    )
    # парсим официальную ZXing страницу, чтобы расшифровать QR
    command_to_exec = [
        "curl",
        "-X", "POST",
        "-F", "f=@" + downloaded_file_name + "",
        "https://zxing.org/w/decode"
    ]
    process = await asyncio.create_subprocess_exec(
        *command_to_exec,
        # stdout must a pipe to be accessible as process.stdout
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    # Wait for the subprocess to finish
    stdout, stderr = await process.communicate()
    e_response = stderr.decode().strip()
    t_response = stdout.decode().strip()
    os.remove(downloaded_file_name)
    if not t_response:
        logger.info(e_response)
        logger.info(t_response)
        await event.edit("Слухай, ты походу что-то сломал... Я не смог расшифровать QR")
        return
    soup = BeautifulSoup(t_response, "html.parser")
    qr_contents = soup.find_all("pre")[0].text
    end = datetime.now()
    ms = (end - start).seconds
    await event.edit("Получено СЕКРЕТНОЕ содержимое QR за {} секунд-ы.\n{}".format(ms, qr_contents))
    await asyncio.sleep(5)
    await event.edit(qr_contents)
 
 
@borg.on(admin_cmd("makeqr ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    input_str = event.pattern_match.group(1)
    message = "кАманда: `.makeqr <ваша мазня>`"
    reply_msg_id = event.message.id
    if input_str:
        message = input_str
    elif event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        reply_msg_id = previous_message.id
        if previous_message.media:
            downloaded_file_name = await borg.download_media(
                previous_message,
                Config.TMP_DOWNLOAD_DIRECTORY,
                progress_callback=progress
            )
            m_list = None
            with open(downloaded_file_name, "rb") as fd:
                m_list = fd.readlines()
            message = ""
            for m in m_list:
                message += m.decode("UTF-8") + "\r\n"
            os.remove(downloaded_file_name)
        else:
            message = previous_message.message
    else:
        message = "кАманда: `.makeqr <ваша мазня>`"
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(message)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("img_file.webp", "PNG")
    await borg.send_file(
        event.chat_id,
        "img_file.webp",
        caption=message,
        reply_to=reply_msg_id,
        progress_callback=progress
    )
    os.remove("img_file.webp")
    end = datetime.now()
    ms = (end - start).seconds
    await event.edit("QR-Code был успешно сделан из говна за {} секунд-ы".format(ms))
    await asyncio.sleep(5)
    await event.delete()