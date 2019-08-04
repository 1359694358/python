import time

from selenium import webdriver

mobile_elements={"deviceName":"iPhone X"} #define a dic  ,declare device model
options=webdriver.ChromeOptions()
# options.add_argument("headless")# 无ui运行
options.add_argument("start-maximize")
options.add_experimental_option("mobileEmulation",mobile_elements)
driver=webdriver.Chrome()#options=options)
driver.implicitly_wait(10)
driver.get("http://www.kuaidi100.com")
driver.find_element_by_id("uDeskTarget").click()
udesk_iframe=driver.find_element_by_id("udesk_iframe")
driver.switch_to.frame("udesk_iframe")
driver.find_element_by_xpath("//textarea[@rows='1']").send_keys("你好")
time.sleep(3)
driver.find_element_by_id("btnSend").click()
time.sleep(8)
driver.quit()