import json
import requests
import re
import nonebot
from nonebot import require
import time
#我写的什么jb
scheduler = require("nonebot_plugin_apscheduler").scheduler
#ac_sig = '_02B4Z6wo00f01YoIXIwAAIDAv5pLXWZID3WKKVgAAAPQKfgQsSI9xS0JOfF3dixTfG4i92vPdSFTS4I9lYCfMe-83rBu4y-8dzNWrmZSpRYMHIXFuL7Vlet-DkAiAS7Hp.5UQSWx2-HBsKysda'
#cookie = '__ac_signature' + ac_sig
cookie = r'_tea_utm_cache_6383=undefined; passport_csrf_token_default=c1b34da5fa251a7c395e699103bf46ba; passport_csrf_token=c1b34da5fa251a7c395e699103bf46ba; MONITOR_DEVICE_ID=99af979a-e19d-4d82-84f0-191533a49080; __ac_nonce=06151cb2200baa17d79f6; __ac_signature=_02B4Z6wo00f01X9yeowAAIDASuBtXn9IM91.U34AAD6RibQ2Jn8X1xe6YZHfA-Ih9pnzT3ooY3CHTFDg.klOeJYPwbSr79JRKzLNQJRV5vNvY3mOLQT.S6SicJkrmejLwalrhD5PFrVvRx-y7c; douyin.com; FOLLOW_YELLOW_POINT_USER=MS4wLjABAAAAGsDNADV8QxdWzkuz14M-7YFhX_WzOnguRPfnaEQy7x1knt6WWivLVcDB7lJIx3WU; FOLLOW_YELLOW_POINT_STATUE_INFO=0%2F1632751571679; msToken=qwPqbL8ojS2Ma9PhM4iUi6Y0WxrZMchg2J9yjuD_vsXstI1JZbSy7M9kmFG188LH87hwDdrztC2ZNsDnq8_VOVeAF50mp8OwOw7YK2dz9Pq3Mh2nfWQYWjycLtJT; s_v_web_id=verify_ku2pfa4t_ZIuDdA1W_Fc0E_4ARh_8fmR_ZnFOygWARiy2; tt_scid=pjFtvJsxkAxtdfChadSOJB1Y2Q4wqWkAVgyzZIJ5tn0pw.I0fdQUOnANkEwh.Snf0101; MONITOR_WEB_ID=5baed6eb-7be5-4fd0-b20c-5dfa8166b938; msToken=6cmbC8MBNDHwhWwx7xqmcBhgH1Y7ZOrw3ck_3Y41g54EGwnB509inuQRtFgcmLHvZ-P6l8Qn7nA-JIDCX_fa54W3zm_zLwvpzbKTygWooLzwnIGNlCtnU46L'
urls = [r"https://www.douyin.com/user/MS4wLjABAAAAxOXMMwlShWjp4DONMwfEEfloRYiC1rXwQ64eydoZ0ORPFVGysZEd4zMt8AjsTbyt",r"https://www.douyin.com/user/MS4wLjABAAAAlpnJ0bXVDV6BNgbHUYVWnnIagRqeeZyNyXB84JXTqAS5tgGjAtw0ZZkv0KSHYyhP",r"https://www.douyin.com/user/MS4wLjABAAAAuZHC7vwqRhPzdeTb24HS7So91u9ucl9c8JjpOS2CPK-9Kg2D32Sj7-mZYvUCJCya",r"https://www.douyin.com/user/MS4wLjABAAAA5ZrIrbgva_HMeHuNn64goOD2XYnk4ItSypgRHlbSh1c",r"https://www.douyin.com/user/MS4wLjABAAAAxCiIYlaaKaMz_J1QaIAmHGgc3bTerIpgTzZjm0na8w5t2KTPrCz4bm_5M5EMPy92"]
uids = [r"MS4wLjABAAAAxOXMMwlShWjp4DONMwfEEfloRYiC1rXwQ64eydoZ0ORPFVGysZEd4zMt8AjsTbyt",r"MS4wLjABAAAAlpnJ0bXVDV6BNgbHUYVWnnIagRqeeZyNyXB84JXTqAS5tgGjAtw0ZZkv0KSHYyhP",r"MS4wLjABAAAAuZHC7vwqRhPzdeTb24HS7So91u9ucl9c8JjpOS2CPK-9Kg2D32Sj7-mZYvUCJCya",r"MS4wLjABAAAA5ZrIrbgva_HMeHuNn64goOD2XYnk4ItSypgRHlbSh1c",r"MS4wLjABAAAAxCiIYlaaKaMz_J1QaIAmHGgc3bTerIpgTzZjm0na8w5t2KTPrCz4bm_5M5EMPy92"]
headers = {
    "Cookie":cookie,
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0'
    }
obj = open(r'.\global.json','rb')
data = json.load(obj)
qqgroup = data['all'] + data['no_shark']
qq_len = len(qqgroup)
names = ['向晚大魔王','贝拉☆kira','珈乐Carol','嘉然今天吃什么','乃琳Queen']

def get_cover(i):
    url = r'https://www.iesdouyin.com/web/api/v2/aweme/post/?sec_uid=' + uids[i]
    s = requests.session()
    resp = s.get(url,headers=headers)
    text = resp.text
    text = json.loads(text)
    awe = text['aweme_list'][0]
    pic = awe['video']['dynamic_cover']['url_list'][0]
    return pic

@scheduler.scheduled_job('interval', minutes=5, id="get_tiktok")
async def main():
    bot = nonebot.get_bot()
    i = -1
    for url in urls:
        i = i + 1
        s = requests.session()
        resp = s.get(url,headers=headers)
        html = resp.text
        html = html.encode()
        h = html.decode('utf-8')
        pattern = re.compile(r'<a href="https://www.douyin.com/video/'+r'\d+')
        n = re.findall(pattern,h)
        try:
            if i == 2:
                new_url = n[1]#珈乐
            else:
                new_url = n[3]#置顶有三个
            n_pattern = re.compile(r'https://www.douyin.com/video/'+r'\d+')
            n_n = re.findall(n_pattern,new_url)
            time.sleep(1)
            req = requests.get(n_n[0],headers=headers)
            htmll = req.text
            htmll = htmll.encode()
            hh = htmll.decode('utf-8')
            new_pattern = re.compile(r'description" content="'+r'.+?'+r'- ',re.S)
            title = re.findall(new_pattern,hh)
            try:
                t = title[0]
                t = re.sub(r'description" content="','',t)
                t = re.sub(r'- ','',t)
            except:
                t = '努力爬取标题中...'
            try:
                name = re.findall(r'- '+r'.+'+r'于',hh,re.U)
                name = str(name[0])
                name = re.sub(r'- ','',name)
                name = re.sub(r'于','',name)
            except:
                name = names[i]
            try:
                cov = get_cover(i)
            except:
                cov = ''
            f = open(r'.\src\assist\{}.txt'.format(name),'r')
            txt = f.read()
            txt = txt.strip()
            #print('n_n',n_n,'txt',txt)
            if n_n[0] == txt:
                f.close()
            else:
                f = open(r'.\src\assist\{}.txt'.format(name),'w')
                f.write(n_n[0])
                f.close()
                rely = [{
                    "type":"text",
                    "data":{
                        "text":"来自" + name + '的抖音小视频：\n' + t + '\n' + n_n[0]
                    }
                },
                {
                "type": "image",
                "data": {
                    "file" : cov
                }
            }
                ]
                for i in range(0,qq_len):
                    await bot.send_group_msg(group_id=qqgroup[i],message=rely)
        except:
            pass