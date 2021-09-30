import json
from bilibili_api import user
from pydantic.types import UUID1
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import nonebot
from selenium.webdriver.common.action_chains import ActionChains
#import cv2
from nonebot import require
from PIL import Image
import re

rids = [0,0,0,0,0,0,0]

obj = open(r'.\global.json','rb')
data = json.load(obj)
qqgroup = data['all']
qq_noshark = data['no_shark']
qq_shark = data['shark']

uid_all = data["asoul_uid"] + data["shark_uid"]
uid_noshark = data["asoul_uid"]

uid_all_len = len(uid_all)
uid_noshark_len = len(uid_noshark)

qq_len = len(qqgroup)
qq_noshark_len = len(qq_noshark)

scheduler = require("nonebot_plugin_apscheduler").scheduler

@scheduler.scheduled_job('interval', minutes=1, id="get_dynamic")
async def main():
    bot = nonebot.get_bot()
    t = time.time()
    t = int(t)
    for i in range (0,uid_all_len):
        u = user.User(uid_all[i])
        global rids   
        page = await u.get_dynamics(0)
        cards = page['cards']
        card = cards[0]
        desc = card['desc']
        rid = desc['dynamic_id']
        ti = desc['timestamp']
        usr_pro = desc['user_profile']
        info = usr_pro['info']
        uname = info['uname']
        c = card['card']
        try:
            item = c['item']
            try:           
                content = item['content']
            except:
                content = item['description']
        except:
            content = ''
        d = '代转'
        d = d.encode('utf-8')
        content = content.encode('utf-8')
        matchobj = re.search(d,content,re.M|re.I)
        ti = int(ti)
        dif = (t - ti)/600  # 10 min
        if rid == rids[i]:
            pass
        elif dif > 1:
            pass
        elif matchobj:
            pass
        else:
            chrome_options = Options()
            chrome_options.add_argument('--headless')
            driver = webdriver.Chrome(executable_path=r'.\src\drivers\chromedriver.exe',chrome_options=chrome_options)
            url = r"https://t.bilibili.com/" + str(rid)
            driver.get(url)
            time.sleep(2)
            driver.set_window_size(1200, 800)
            action = ActionChains (driver)
            action.move_by_offset(656,96).perform()
            time.sleep(0.5)
            actions = ActionChains (driver)
            actions.move_by_offset(-300,0).perform()
            time.sleep(3)
            path = r"C:\Users\Administrator\Desktop\Asoul-bot\go-cqhttp\data\images\{}.png".format(rid)
            driver.get_screenshot_as_file(path)
            driver.quit()       
            """ img = cv2.imread(path)
            cut = img[70:730, 300:900] #change the size here
            cv2.imwrite(path, cut) """
            img= Image.open(path)
            cut = img.crop((275,65,910,800))
            cut.save(path)
            """ rely ={
                "type": "text",
                "data": {
                    "text": "来自" + uname + "的动态：\n" + url + '\n'
                    }
                } """
                #{
                   # "type": "image",
                    #"data": {
                      #  "file": r"///C:\Users\13591\Desktop\Asoul-bot\go-cqhttp\data\images\{}.png".format(rid)
                    #}
                #}
                #]
            rely = "来自" + uname + "的动态：\n" + url + '\n'
            img_path = r'C:\Users\Administrator\Desktop\Asoul-bot\go-cqhttp\data\images\{}.png'.format(rid)
            cq = r'[CQ:image,file=file:///' + str(img_path) + ']'
            if i == 6:
                rids[i] = rid
                await bot.send_group_msg(group_id=qq_shark[0],message=rely+cq)
                for j in range(0,qq_len):  
                    await bot.send_group_msg(group_id=qqgroup[j],message=rely+cq)
            else:
                for k in range(0,qq_len):
                    rids[i] = rid
                    await bot.send_group_msg(group_id=qqgroup[k],message=rely+cq)
                for m in range(0,qq_noshark_len):
                    rids[i] = rid
                    await bot.send_group_msg(group_id=qq_noshark[m],message=rely+cq)