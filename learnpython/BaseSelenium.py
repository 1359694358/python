import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseSelenium(object):
    Chrome=1
    FireFox=2
    def __init__(self,browserType=Chrome):
        if browserType==BaseSelenium.Chrome:
            self.driver=webdriver.Chrome()
        else:
            self.driver=webdriver.Firefox()
        self.wait_timeout=10
        self.wait_check_inteval=0.5
        return


    def openUrl(self,url):
        self.driver.get(url)
        return


    def setImplicitlyWaitTime(self,time):
        self.driver.implicitly_wait(time)
        return

    def findElement(self,by,value):
        return self.driver.find_element(by,value)

    def waitFindElement(self,findElement_method):
        print("waitFindElement")
        waitResult= WebDriverWait(self.driver,self.wait_timeout,self.wait_check_inteval).until(method=findElement_method)
        return waitResult

    def waitFindElementByValue(self,by,value):
        print("waitFindElement")
        waitResult= WebDriverWait(self.driver,self.wait_timeout,self.wait_check_inteval).until(EC.visibility_of_element_located((by,value)))
        return waitResult

    def clickElement(self,by,value):
        self.waitFindElement(EC.visibility_of_element_located((by,value))).click()
        return

    def inputElement(self,by,value,sendValue):
        self.waitFindElement(EC.visibility_of_element_located((by,value))).send_keys(sendValue)
        return

    def move2Element(self,by,value):
        element=self.waitFindElement(EC.visibility_of_element_located((by,value)))
        print(element)
        ActionChains(self.driver).move_to_element(element).perform()
        return

    def openNewTable(self,url):
        js='window.open("{}")'.format(url)
        print(js)
        self.driver.execute_script(js)
        return

    def switch_to_iframe(self,value):
        self.driver.switch_to.frame(value)
        return
    def switch_to_default_content(self):
        self.driver.switch_to.default_content()
        return
    def forceWait(self,t):
        time.sleep(t)
        return

    def switch_table(self,index):
        handles=self.driver.window_handles
        first=handles[0]
        handles.remove(handles[0])
        handles.append(first)
        handles.reverse()
        self.driver.switch_to.window(handles[index])
        print(type(handles),handles)

    def quit(self):
        self.driver.quit()
        return
    def close(self):
        self.driver.close()
        return

