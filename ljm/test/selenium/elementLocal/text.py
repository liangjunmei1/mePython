#coding=utf-8
'''
Created on 2017年1月26日

@author: Administrator
'''

import os
from selenium import webdriver

firefoxBin = os.path.abspath(r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe")
os.environ["webdriver.firefox.bin"] = firefoxBin

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

value = driver.find_element_by_id("setf").text
print value

driver.quit()