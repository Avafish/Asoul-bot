# -*- coding: utf-8 -*-
from nonebot import on_command
import random
from nonebot.adapters import Bot, Event
from nonebot.rule import to_me
import json



joke = on_command('冷笑话', aliases={'笑话'}, rule=to_me(), priority=1)

@joke.handle()
async def _(bot: Bot, event: Event):
    obj = open(r'.\src\assist\joke.json', 'r',encoding=('utf-8'))
    jokes = json.load(obj)['jokes']
    i = len(jokes)
    j = random.randint(0, i-1)
    await joke.finish(message=jokes[j])