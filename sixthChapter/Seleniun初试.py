from selenium import webdriver

import time

driver=webdriver.Chrome()#实例化一个浏览器对象
url='https://www.baidu.com'
driver.get(url)#让浏览器发起一个指定url的对应请求
time.sleep(10)
driver.close()