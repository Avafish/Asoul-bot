import json
import random
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.adapters import Bot, Event

dis = on_command('发病', rule=to_me(), priority=1)

obj = open(r'.\src\assist\disease.json','r',encoding=('utf-8'))
data = json.load(obj)
begin = data['begin']
follow = data['follow']
aw = data['aw']
emoji = data['emoji']
sth = data['sth']
ath = data['ath']
dosth = data['dosth']
name = data['name']
dxw = data['dxw']

def ran(ilist):
    random.shuffle(ilist)
    return ilist[0]

@dis.handle()
async def _(bot: Bot, event: Event):
    usrmsg = str(event.get_message()).replace('发病','').replace(' ','')
    if usrmsg == '':
        k = random.random()
        if k<0.5:
            tmp = str()
            tmp += ran(begin) + '，'
            tmp += ran(aw)*3 + '，'
            tmp += ran(follow)

            tmp = tmp.replace("xx",ran(name))
            tmp = tmp.replace("sth",ran(sth))
            tmp = tmp.replace("ath",ran(ath))
            tmp = tmp.replace("doth",ran(dosth))
            tmp = tmp.replace("+",ran(emoji))
            await dis.send(message=tmp)
        else:
            tmp = str()
            tmp += ran(dxw)
            tmp = tmp.replace("name",ran(name))
            await dis.send(message=tmp)
    else:
        tmp = str()
        tmp += ran(dxw)
        tmp = tmp.replace("name",usrmsg)
        await dis.send(message=tmp)
