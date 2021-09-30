from hashlib import md5
from nonebot import on_command
import hashlib
from nonebot.adapters import Bot, Event
from nonebot.rule import to_me
import re

remake = on_command('匹配', rule=to_me())

@remake.handle()
async def _(bot: Bot, event: Event):
    usrname = event.get_user_id()
    #usrmsg = str(event.get_message()).replace('匹配','').replace(' ','')
    usrmsg = str(event.get_message()).replace(' ','')
    if usrmsg != '':
        #txt = usrname + usrmsg
        txt = usrmsg
        md5_con = md5(txt.encode('utf8')).hexdigest()
        s = [i for i in md5_con if i.isnumeric()]
        s = "".join(s)
        sha_con = hashlib.sha1(txt.encode('utf8')).hexdigest()
        t = [j for j in sha_con if j.isnumeric()]
        t = "".join(t)
        result = int(s) + int(t)
        usrname = int(usrname)
        rp = (result + usrname)%101

        rely = [{
            "type": "at",
            "data": {
                "qq": usrname,
                "name": ""
            }
        },
        {
                "type": "text",
                "data": {
                    "text": "\n" + "嗨呀，你和" + str(usrmsg) + "的相配程度竟然是" + str(rp) + '%呀！'
                }
        }
        ]

        await remake.finish(message=rely)
    else:
        await remake.reject(message="格式不对啦，请加空格和匹配对象")