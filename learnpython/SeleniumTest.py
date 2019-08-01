import time

from selenium import webdriver

mobile_elements={"deviceName":"iPhone X"} #define a dic  ,declare device model
options=webdriver.ChromeOptions()
# options.add_argument("headless")# 无ui运行
options.add_argument("start-maximize")
options.add_experimental_option("mobileEmulation",mobile_elements)
driver=webdriver.Chrome(options=options)
driver.implicitly_wait(10)
driver.get("http://127.0.0.1:5000")
# driver.find_element_by_id("testid").click()
# driver.switch_to.alert.accept()
# driver.switch_to.default_content()
print(type(driver.find_elements_by_tag_name("input")))
driver.find_element_by_class_name("testclassname").click()
driver.switch_to.alert.accept()
# xpath的特殊用法
#$x("//a[contains(text(),'移动')]")
#$x("//a[starts-with(text(),'练习')]")
driver.find_element_by_xpath("//a[@href='/signin']").click()

#svg  name='svg'
#$x("//*[name()='svg']")

driver.find_element_by_name("username").send_keys("15902127953")
driver.find_element_by_name("password").send_keys("123456")
driver.find_element_by_xpath("/html/body/form/p[3]/button").click()
print(driver.window_handles)
# driver.back()
time.sleep(3)
driver.execute_script("window.open('https://www.baidu.com')")
print(driver.window_handles)
# print(driver.page_source)
driver.refresh()
driver.maximize_window()
driver.execute_script("window.open('http://127.0.0.1:5000')")
time.sleep(2)
driver.execute_script("window.open('http://www.163.com')")
time.sleep(2)
driver.execute_script("window.open('http://www.sina.com')")
time.sleep(2)
print("current;",driver.current_window_handle)
print(driver.title)
handles=driver.window_handles
print("handles:",handles)
time.sleep(2)
for handle in handles:
    print("handle:{}".format(handle))
    driver.switch_to.window(handle)
    print(driver.title)
time.sleep(3)
driver.close()
time.sleep(2)
driver.quit()