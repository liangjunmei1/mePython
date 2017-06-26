#coding=utf-8
'''
Created on 2017年1月26日

@author: Administrator
'''

import os,time
from selenium import webdriver

firefoxBin = os.path.abspath(r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe")
os.environ["webdriver.firefox.bin"] = firefoxBin

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
driver.find_element_by_link_text("新闻").click()

time.sleep(5)
driver.back() #退回到百度首页
time.sleep(5)
driver.forward() #前进到新闻页面
time.sleep(5)

driver.quit()
