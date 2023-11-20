from selenium import webdriver
import time

driver=webdriver.Chrome()#实例化一个浏览器对象
url='https://www.alibaba.com'
driver.get(url)#让浏览器发起一个指定url的对应请求

searchInput=driver.find_element_by_css_selector('.search-bar-input')#标签定位
searchInput.send_keys('sofa')#标签交互

btn=driver.find_element_by_css_selector('.fy23-icbu-search-bar-inner-button')#标签定位
btn.click()#标签操作

driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')#执行js程序
time.sleep(2)

driver.get('https://www.baidu.com')
time.sleep(2)

driver.back()#回退，点击返回按钮
time.sleep(2)

driver.forward()#前进


driver.close()
