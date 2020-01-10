from selenium import webdriver
import time
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

#获取driver
driver = webdriver.Chrome()

#打开网页
driver.get("https://xdclass.net")
print(driver.title)
sleep(2)

#获取登录框
login_ele = driver.find_element_by_css_selector("#app > div > div.header > div > div.r_userinfo.f_r > div.avatar.f_r > img")
#触发点击事件
ActionChains(driver).click(login_ele).perform()


