#mod by Anonumyc Economy Team

"""
Поисковик такие как -> Google / YouTube / DuckDuckGo / GitHub / RBC / Xvideo / Xvideos2/ Pornhub / var / log / Dyno.

Какие кАманды и за что они отвечают?

.lmg <поисковый запрос Google>

.lmy <поисковый запрос YouTube>
 
.lmd <поисковый запрос DuckDuckGo>
 
.lmw <поиск в Wikipedia>
 
.lmgit <поиск репозитория в GitHub>

.lmnews <поиск новостей>

.lmx <поиск xvideos>
 
.lmx2 <поиск xvideos2>

.lmp <поиск pornhub>

.lmvar <название приложения heroku настройки>

.lmlog <название приложения heroku логи>

.dyno <тип биллинга>
 



"""







from telethon import events



import os



import requests



import json



from uniborg.util import admin_cmd











@borg.on(admin_cmd(pattern="lmg (.*)"))



async def _(event):



    if event.fwd_from:



        return



    input_str = event.pattern_match.group(1)



    sample_url = "https://da.gd/s?url=http://google.com/search?q={}".format(input_str.replace(" ","+"))



    response_api = requests.get(sample_url).text



    if response_api:



        await event.edit("Я нашёл твой запрос в **Google** который ты просил:\n👉 [{}]({})\n`Вот тот самый запрос... 😉` ".format(input_str,response_api.rstrip()))



    else:



        await event.edit("Эм.. Ты всё верно дядь вёл?...")





@borg.on(admin_cmd(pattern="lmy (.*)"))



async def _(event):



    if event.fwd_from:



        return



    input_str = event.pattern_match.group(1)



    sample_url = "https://da.gd/s?url=https://www.youtube.com/results?search_query={}".format(input_str.replace(" ","+"))



    response_api = requests.get(sample_url).text



    if response_api:



        await event.edit("Я нашёл твой запрос в **YouTube** который ты просил:\n👉 [{}]({})\n`Вот тот самый запрос... 😉` ".format(input_str,response_api.rstrip()))


    else:



        await event.edit("Эм.. Ты всё верно дядь вёл?...")




@borg.on(admin_cmd(pattern="lmd (.*)"))



async def _(event):



    if event.fwd_from:



        return



    input_str = event.pattern_match.group(1)



    sample_url = "https://da.gd/s?url=https://duckduckgo.com/?q={}&t=h_&ia=about".format(input_str.replace(" ","+"))



    response_api = requests.get(sample_url).text



    if response_api:



        await event.edit("Я нашёл твой запрос в **DuckDuckGo** который ты просил:\n👉 [{}]({})\n`Вот тот самый запрос... 😉` ".format(input_str,response_api.rstrip()))



    else:



        await event.edit("Эм.. Ты всё верно дядь вёл?...")




@borg.on(admin_cmd(pattern="lmx (.*)"))



async def _(event):



    if event.fwd_from:



        return



    input_str = event.pattern_match.group(1)



    sample_url = "https://da.gd/s?url=https://www.xvideos.com/?k={}".format(input_str.replace(" ","+"))



    response_api = requests.get(sample_url).text



    if response_api:



        await event.edit("Я нашёл твой запрос в **xvideos** который ты просил:\n👉 [{}]({})\n`Вот тот самый запрос... 😉 Только не в мясо, окей?)` ".format(input_str,response_api.rstrip()))



    else:



        await event.edit("Эм.. Ты всё верно дядь вёл?...")




@borg.on(admin_cmd(pattern="lmp (.*)"))



async def _(event):



    if event.fwd_from:



        return



    input_str = event.pattern_match.group(1)



    sample_url = "https://da.gd/s?url=https://www.pornhub.com/video/search?search={}".format(input_str.replace(" ","+"))



    response_api = requests.get(sample_url).text



    if response_api:



        await event.edit("Я нашёл твой запрос в **PornoHub** который ты просил:\n👉 [{}]({})\n`Вот тот самый запрос... 😉 И да, лучше найди себе пару...` ".format(input_str,response_api.rstrip()))



    else:



        await event.edit("Эм.. Ты всё верно дядь вёл?...")


@borg.on(admin_cmd(pattern="lmnews (.*)"))



async def _(event):



    if event.fwd_from:



        return



    input_str = event.pattern_match.group(1)



    sample_url = "https://da.gd/s?url=https://www.rbc.ua/rus/search?search_text={}".format(input_str.replace(" ","+"))



    response_api = requests.get(sample_url).text



    if response_api:



        await event.edit("Я нашёл твой запрос в **RBC** который ты просил:\n👉 [{}]({})\n`Вот тот самый запрос... 😉` ".format(input_str,response_api.rstrip()))



    else:



        await event.edit("Эм.. Ты всё верно дядь вёл?...")



@borg.on(admin_cmd(pattern="lmvar (.*)"))



async def _(event):



    if event.fwd_from:



        return



    input_str = event.pattern_match.group(1)



    sample_url = "https://da.gd/s?url=https://dashboard.heroku.com/apps/{}/settings".format(input_str.replace(" ","+"))



    response_api = requests.get(sample_url).text



    if response_api:



        await event.edit("Я нашёл твой запрос в **VAT** который ты просил:\n👉 [{}]({})\n`Вот тот самый запрос... 😉` ".format(input_str,response_api.rstrip()))



    else:



        await event.edit("Эм.. Ты всё верно дядь вёл?...")



@borg.on(admin_cmd(pattern="lmlog (.*)"))



async def _(event):



    if event.fwd_from:



        return



    input_str = event.pattern_match.group(1)



    sample_url = "https://da.gd/s?url=https://dashboard.heroku.com/apps/{}/logs".format(input_str.replace(" ","+"))



    response_api = requests.get(sample_url).text



    if response_api:



        await event.edit("Я нашёл твой запрос в **LOG** который ты просил:\n👉 [{}]({})\n`Вот тот самый запрос... 😉` ".format(input_str,response_api.rstrip()))



    else:



        await event.edit("Эм.. Ты всё верно дядь вёл?...")

        
        
@borg.on(admin_cmd(pattern="lmx2 (.*)"))



async def _(event):



    if event.fwd_from:



        return



    input_str = event.pattern_match.group(1)



    sample_url = "https://da.gd/s?url=https://www.xvideos2.com/?k={}".format(input_str.replace(" ","+"))



    response_api = requests.get(sample_url).text



    if response_api:



        await event.edit("Я нашёл твой запрос в **xvideos2** который ты просил:\n👉 [{}]({})\n`Вот тот самый запрос... 😉 Удачи поматать ствол)` ".format(input_str,response_api.rstrip()))



    else:



        await event.edit("Эм.. Ты всё верно дядь вёл?...")
        
      


@borg.on(admin_cmd(pattern="dyno(.*)"))



async def _(event):



    if event.fwd_from:



        return



    input_str = event.pattern_match.group(1)



    sample_url = "https://da.gd/s?url=https://dashboard.heroku.com/account/{}".format(input_str.replace(" ","+"))



    response_api = requests.get(sample_url).text



    if response_api:



        await event.edit("Я нашёл твой запрос в **Dyno** который ты просил:\n👉 [{}]({})\n`Вот тот самый запрос... 😉` ".format(input_str,response_api.rstrip()))



    else:



        await event.edit("Эм.. Ты всё верно дядь вёл?...")
      
@borg.on(admin_cmd(pattern="lmgit(.*)"))



async def _(event):



    if event.fwd_from:



        return



    input_str = event.pattern_match.group(1)



    sample_url = "https://da.gd/s?url=https://github.com/search?q={}".format(input_str.replace(" ","+"))



    response_api = requests.get(sample_url).text



    if response_api:



        await event.edit("Я нашёл твой запрос в **GitHub** который ты просил вот и репозитория:\n👉 [{}]({})\n`Вот тот самый запрос... 😉` ".format(input_str,response_api.rstrip()))



    else:



        await event.edit("Эм.. Ты всё верно дядь вёл?...")

@borg.on(admin_cmd(pattern="lmw(.*)"))



async def _(event):



    if event.fwd_from:



        return



    input_str = event.pattern_match.group(1)



    sample_url = "https://da.gd/s?url=https://ru.wikipedia.org/wiki/{}".format(input_str.replace(" ","_"))



    response_api = requests.get(sample_url).text



    if response_api:



        await event.edit("Я нашёл твой запрос в **Wikipedia** который ты просил:\n👉 [{}]({})\n`Вот тот самый запрос... 😉 Нy... Хоть чем-то интересуешься)` ".format(input_str,response_api.rstrip()))



    else:



        await event.edit("Эм.. Ты всё верно дядь вёл?...")