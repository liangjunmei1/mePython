#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains    #引入鼠标事件所需模块
import time,os
#访问百度
driver=webdriver.Firefox()
driver.get("http://127.0.0.1:8013/iwebshop")
driver.maximize_window()

title = driver.title
print title
#获得开源电子商务的innerHTML属性值并打印
#a = driver.find_element_by_link_text("开源电子商务").get_attribute("innerHTML")
#print a

#鼠标悬停在对象：去结算，提示金额信息
above = driver.find_element_by_link_text(u"去结算")
ActionChains(driver).move_to_element(above).perform()


#driver.find_element_by_id("su1").click()
time.sleep(3)

'''
#将滚动条移动到页面的顶部
js_="var q=document.documentElement.scrollTop=100"
driver.execute_script(js_)
time.sleep()
#将页面滚动条拖到底部
js="var q=document.documentElement.scrollTop=1000"
driver.execute_script(js)
'''
print 'ok'
time.sleep(1)
driver.quit()
os.system("pause")