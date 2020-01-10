import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

#获取driver
chromedriver = "/usr/local/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
#隐形等待，最长等待10秒,只需设置一次

driver.implicitly_wait(10)

#打开网页
driver.get("http://baidu.com")

#显性等待
#5:最长等待时间，0.5:监测时间，每隔0.5监测一次
#每隔0.5秒查找一次id为kw的元素，最长等待时间为5秒，若找不到则抛出异常
#系统抛出异常，并试图捕捉异常
try:
    ele = WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.ID,"kw")))
    ele.send_keys("小D课堂")
    sleep(3)
    print("资源加载成功")
    print(driver.title)
except:
    print("资源加载失败")
finally:
    print("不管是否成功，都会执行")
    #清理资源，退出浏览器
    driver.quit()
