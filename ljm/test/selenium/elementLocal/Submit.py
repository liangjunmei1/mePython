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

driver.find_element_by_id("kw").clear()
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").submit()

time.sleep(3)
driver.quit()

