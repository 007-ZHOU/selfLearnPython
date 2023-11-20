from selenium  import webdriver
import time
from selenium.webdriver.chrome.options import Options#实现无可视化界面的
from selenium.webdriver import ChromeOptions#实现规避检测
#实现无可视化界面的操作
chrome_options=Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

#如何实现让selenium规避被检测到的风险
option=ChromeOptions()
option.add_experimental_option('excludeSwithes',['enable-automation'])

driver=webdriver.Chrome(chrome_options=chrome_options,options=option)
#无可视化界面
url='https://www.baidu.com'
driver.get(url=url)

print(driver.page_source)
time.sleep(2)
driver.close()