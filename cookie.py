from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

#获取driver
driver = webdriver.Firefox()
#隐形等待，最长等待10秒,只需设置一次
driver.implicitly_wait(10)

#打开网页
driver.get("https://xdclass.net")

print(driver.title)

sleep(2)