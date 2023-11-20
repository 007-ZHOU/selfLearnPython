from selenium  import webdriver
import time
from selenium.webdriver import ActionChains

driver=webdriver.Chrome()
driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
#如果定位的标签是存在与iframe标签之中，则必须通过如下操作进行标签定位
driver.switch_to.frame('iframeResult')#切换浏览器标签定位的作用域
div=driver.find_element_by_id('draggable')
print(div)

#动作链，进行拖到操作
aciton=ActionChains(driver)#实例化，class
#点击长按指定的标签
aciton.click_and_hold(div)
for i in range(5):
    aciton.move_by_offset(xoffset=17,yoffset=0).perform()
    time.sleep(0.1)
aciton.release()#释放动作链

time.sleep(3)
driver.close()