import nonebot
from selenium import webdriver
import time
import json

qqgroup = 752408143
@nonebot.scheduler.scheduled_job('interval', hours=12)
async def main():
    bot = nonebot.get_bot()
    title = []
    driver = webdriver.Chrome(executable_path=r'C:\drivers\chromedriver.exe')
    url = r'https://asoul.icu/articles'
    driver.get(url)
    time.sleep(3)
    while True:
        try:
            element = driver.find_element_by_class_name("btn-block")
            element.click()
            time.sleep(3)
        except:
            list = driver.find_elements_by_class_name("card-title.title-limits")
            for i in list:
                title.append(i.text)
            obj = open(r'C:\Users\Administrator\Desktop\luciabot\lucia\bot_plugins\assist\xzw.json','w')
            json.dump(title,obj)
            driver.quit()
            break
    await bot.send_group_msg(group_id=qqgroup,message = '小作文 updated')