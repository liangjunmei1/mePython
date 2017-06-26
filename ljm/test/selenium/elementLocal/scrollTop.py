#coding=utf-8
'''
Created on 2017年1月27日

@author: Administrator
'''
import os,time
from selenium import webdriver

firefoxBin = os.path.abspath(r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe")
os.environ["webdriver.firefox.bin"] = firefoxBin

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
#搜索
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
time.sleep(3)

#将滚动条拖动到最底部
js="var q=document.documentElement.scrollTop=10000"
driver.execute_script(js)
time.sleep(2)

#将滚动条拖动到最顶部
js="var q=document.documentElement.scrollTop=0"
driver.execute_script(js)
time.sleep(2)

driver.quit()