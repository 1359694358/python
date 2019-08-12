import re
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from dy.selenium.yamlhandle import readYml


class SeleniumToolKit(object):
    def __init__(self,browser_cfgpath=None):
        if browser_cfgpath != None:
            config=readYml(browser_cfgpath)
            print(config)
            type=config['type']
            driverpath=config['driverpath']
            isChrome=bool(re.search('chrome',type,re.IGNORECASE))
            isFireFox = bool(re.search('fire', type, re.IGNORECASE))
            if isChrome:
                if not driverpath:
                    driverpath='chromedriver'
                self.driver = webdriver.Chrome(executable_path=driverpath)
            elif isFireFox:
                if not driverpath:
                    driverpath='geckodriver'
                self.driver = webdriver.Firefox(executable_path=driverpath)
            position=config['position']
            size=config['size']
            mode=config['mode']
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
        waitResult= WebDriverWait(self.driver,self.wait_timeout,self.wait_check_inteval).until(method=findElement_method)
        return waitResult

    def waitFindElementByValue(self,by,value):
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

    def switch_table_by_title(self,title):
        handles=self.driver.window_handles
        for itemHandle in handles:
            self.driver.switch_to.window(itemHandle)
            tableTitle =self.driver.title
            if title in tableTitle:
                break
        return

    def switch_table_by_index(self,index):
        handles=self.driver.window_handles
        self.driver.switch_to.window(handles[index])
        return

    def switch_table_by_url(self,url):
        handles=self.driver.window_handles
        for itemHandle in handles:
            self.driver.switch_to.window(itemHandle)
            curUrl =self.driver.current_url
            if url in curUrl:
                break
        return

    def quit(self):
        self.driver.quit()
        return
    def close(self):
        self.driver.close()
        return
