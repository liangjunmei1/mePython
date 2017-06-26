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
driver.maximize_window()
driver.set_window_size(400, 500)
driver.implicitly_wait(3)

driver.get("http://www.baidu.com")
print driver.title

