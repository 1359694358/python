# -*- coding: utf-8 -*-
import yaml
from selenium import webdriver


def read_yaml():
    '''
    读取yaml配置文件
    :return: cfg
    '''
    with open("./data.yaml", 'r', encoding="UTF-8") as yamlfile:
        cfg = yaml.load(yamlfile, Loader=yaml.FullLoader)
        url = cfg['url']
        browser_type = cfg['browser']['type']
        browser_mode = cfg['browser']['mode']
        print(url, browser_type, browser_mode)
        return cfg


# read_yaml()


def open_browser():
    '''
    设置浏览器属性
    :return: 返回浏览器实例
    '''
    cfg = read_yaml()
    options = webdriver.ChromeOptions()
    if cfg['browser']['mode'] == 'headless':
        options.add_argument('headless')  # 设置无头浏览器
        options.add_argument('start-maximized')  # 最大化浏览器
        options.add_argument('disable-infobars')  # 去除浏览器黄条
    if cfg['browser']['type'] == 'ie':
        browser = webdriver.Ie()
    if cfg['browser']['type'] == 'firefox':
        browser = webdriver.Firefox()
    if cfg['browser']['type'] == 'chrome':
        browser = webdriver.Chrome(options=options)
    else:
        raise ('浏览器类型错误')
    browser.get(cfg['url'])
    return browser
