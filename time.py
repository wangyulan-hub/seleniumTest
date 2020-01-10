from selenium import webdriver
from time import sleep

#获取driver
driver = webdriver.Chrome()
#隐形等待，最长等待10秒,只需设置一次
driver.implicitly_wait(10)

#打开网页
driver.get("http://baidu.com")

#强制等待10秒
# sleep(10)

print(driver.title)

