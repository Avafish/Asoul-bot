import re
from nonebot import on_regex
from nonebot.adapters import Bot, Event
import requests

headers = {
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0'
    }
#analysis_bili = on_regex(r"(b23.tv)|(bili(22|23|33|2233).cn)|(live.bilibili.com)|(bilibili.com/(video|read|bangumi))|(^(av|cv)(\d+))|(^BV([a-zA-Z0-9])+)|(\[\[QQ小程序\]哔哩哔哩\])|(QQ小程序&amp;#93;哔哩哔哩)|(QQ小程序&#93;哔哩哔哩)", flags=re.I)
analysis_bili = on_regex(r"(b23.tv)|(bilibili.com/video)|(^BV([a-zA-Z0-9])+)", flags=re.I)
@analysis_bili.handle()
async def analysis_main(bot: Bot, event: Event, state: dict):
    text = str(event.get_message()).strip()
    if re.search(r"^BV([a-zA-Z0-9])+", text, re.I):
        text = r'https://www.bilibili.com/video/' + text
    resp = requests.get(text,headers=headers)
    t = resp.text
    title = re.findall(r'name="title" content="'+r'.+?'+r'_哔哩哔哩_bilibili">',t)
    title = re.sub(r'name="title" content="','',title[0])
    title = re.sub(r'_哔哩哔哩_bilibili">','',title)
    up = re.findall(r'","name":"'+r'.+?'+r'","approve":',t)
    up = re.sub(r'","name":"','',up[0])
    up = re.sub(r'","approve":','',up)
    pic = re.findall(r'itemprop="image" content="'+r'.+?'+r'><meta',t)
    pic = re.sub(r'itemprop="image" content="','',pic[0])
    pic = re.sub(r'"><meta','',pic)
    rely = [
            {
            "type": "text",
            "data": {
                "text": '标题：' + title + '\n' + 'up主：' + up + '\n'
            }
        },
            {
            "type": "image",
            "data": {
                "file" : pic
            }
        }]
    await analysis_bili.finish(message=rely)