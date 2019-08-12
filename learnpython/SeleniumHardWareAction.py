from selenium import webdriver
# keyboard action
from selenium.webdriver.common.keys import Keys

import time
driver=webdriver.Chrome()
driver.get("http://127.0.0.1:5000/signin")
driver.find_element_by_name("username").send_keys("15902127953")
driver.find_element_by_name("username").send_keys(Keys.TAB)
time.sleep(2)
driver.find_element_by_name("password").send_keys("123456")
driver.find_element_by_name("password").send_keys(Keys.ENTER)

time.sleep(2)
driver.back()
'''
    左键按下不放 
    双击
    移动到元素
    拖拽
    松开
'''

from selenium.webdriver.common.action_chains import ActionChains

moveElement=driver.find_element_by_partial_link_text("移动")
ActionChains(driver).move_to_element(moveElement).perform()

time.sleep(2)

driver.find_element_by_partial_link_text("拖拽").click()
dragger=driver.find_element_by_id("dragger")
ActionChains(driver).click_and_hold(dragger).perform()
time.sleep(2)
ActionChains(driver).release(dragger).perform()
item=driver.find_element_by_xpath("//*[text()='Item 3']")
print(item)
ActionChains(driver).drag_and_drop(dragger,item).perform()

time.sleep(3)

driver.get("http://sahitest.com/demo/dragDropMooTools.htm")



driver.quit()