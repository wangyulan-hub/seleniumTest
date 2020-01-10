from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

#获取driver
driver = webdriver.Chrome()
#隐形等待，最长等待10秒,只需设置一次
driver.implicitly_wait(10)

#打开网页
driver.get("http://localhost:63342/seleniumTest/radio.html?_ijt=t623g5juj3mmj1l5skeglatvmr")

print(driver.title)

sleep(2)

#两秒后选择female
driver.find_element_by_id("female").click()
