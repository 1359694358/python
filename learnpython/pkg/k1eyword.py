# -*- coding: utf-8 -*-
from pkg import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MKeyWord():
    def __init__(self):
        self.browser = browser.open_browser()

    def into_frame(self, value):
        '''
        进入frame
        :param value:
        :return:
        '''
        self.browser.switch_to_frame(value)

    def out_frame(self):
        '''
        退出frame
        :return:
        '''
        self.browser.switch_to_default_content()

    def click_element_By_X(self, method, value):
        '''
        等待元素出现，并进行点击操作
        :param method:
        :param value:
        :return:
        '''
        element = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((method, value)))
        element.click()

    def input_element_By_X(self, method, value, value1):
        '''
        等待元素出现，并进入输入操做
        :param method:
        :param value:
        :param value1:
        :return:
        '''
        element = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((method, value)))
        element.send_keys(value1)

    def close_browser(self):
        '''
        关闭浏览器
        :return:
        '''
        self.browser.quit()

    def get_text_By_X(self, method):
        '''
        根据传入的定位方法获取该路径的文本值
        :param method:
        :return:
        '''
        self.browser.find_element(method).text

    def get_url(self):
        self.browser.current_url

    def case(self):
        self.input_element_By_X(By.ID, 'kw', '123')
        # self.get_url()
        self.close_browser()


A = MKeyWord()
A.case()