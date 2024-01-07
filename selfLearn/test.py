# -*- coding: utf-8 -*-
import time
import random
from selenium import webdriver
 
 
class SetProxyModel():
    test_url = "http://httpbin.org/ip"
 
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument(
            'user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"')
        # 设置代理
        self.proxy = '125.87.104.255:22015'
        self.options.add_argument('--proxy-server=' + self.proxy)
        self.driver = webdriver.Chrome(
            options=self.options)
        self.driver.maximize_window()
 
    def set_proxy(self):
        self.driver.get(self.test_url)

 
if __name__ == '__main__':
    sp = SetProxyModel()
    sp.set_proxy()
