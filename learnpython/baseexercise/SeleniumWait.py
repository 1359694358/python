import time

from selenium import webdriver

mobile_elements={"deviceName":"iPhone X"} #define a dic  ,declare device model
options=webdriver.ChromeOptions()
# options.add_argument("headless")# 无ui运行
options.add_argument("start-maximize")
options.add_experimental_option("mobileEmulation",mobile_elements)
driver=webdriver.Chrome()
driver.implicitly_wait(50)
driver.get("http://www.zzu.edu.cn/?tdsourcetag=s_pcqq_aiomsg")
print(driver.find_element_by_xpath('//*[@id="header_big_nav"]/li[3]'))
time.sleep(3)
driver.close()
driver.quit()