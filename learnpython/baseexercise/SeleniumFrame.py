import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


mobile_elements={"deviceName":"iPhone X"} #define a dic  ,declare device model
options=webdriver.ChromeOptions()
# options.add_argument("headless")# 无ui运行
options.add_argument("start-maximize")
options.add_experimental_option("mobileEmulation",mobile_elements)
driver=webdriver.Chrome()#options=options)
# driver.implicitly_wait(10)
driver.get("http://www.kuaidi100.com")


uDeskTarget=WebDriverWait(driver,10,0.5).until(lambda dri:dri.find_element(By.ID,"uDeskTarget"))
uDeskTarget.click()
# uDeskTarget=WebDriverWait(driver,10,0.5).until(EC.visibility_of_element_located((By.ID,"uDeskTarget")))
# uDeskTarget.click()



def findEle(dri):
    print("find ele",type(dri))
    return dri.find_element(By.XPATH,"//textarea[@rows='1']")

# driver.find_element_by_id("uDeskTarget").click()
# udesk_iframe=driver.find_element_by_id("udesk_iframe")
driver.switch_to.frame("udesk_iframe")
WebDriverWait(driver,20,0.3).until(lambda dri:dri.find_element(By.XPATH,"//textarea[@rows='1']")).send_keys("hello world")
# input=WebDriverWait(driver,10,0.5).until(EC.visibility_of_element_located((By.XPATH,"//textarea[@rows='1']")))
# driver.find_element_by_xpath("//textarea[@rows='1']").send_keys("你好")
# input.send_keys("hello world")
# time.sleep(3)
# driver.find_element_by_id("btnSend").click()
driver.switch_to.default_content()
time.sleep(8)
driver.quit()

from selenium.webdriver.support.select import Select

# Select(element).select_by_index()