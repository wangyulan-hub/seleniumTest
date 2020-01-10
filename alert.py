#弹窗的处理

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

#获取driver
driver = webdriver.Chrome()
#隐形等待，最长等待10秒,只需设置一次
driver.implicitly_wait(10)

#打开网页
driver.get("http://localhost:63342/seleniumTest/alert.html?_ijt=m4vq2v16g2ib71qktfs3tfqskg")

print(driver.title)

sleep(2)

driver.find_element_by_id("alert").click()

#切换到弹窗
win = driver.switch_to_alert()

sleep(2)
#点击确定
win.accept()

sleep(2)

driver.find_element_by_id("confirm").click()
confrim_ele = driver.switch_to_alert()

sleep(2)
#点击取消
confrim_ele.dismiss()

driver.quit()


