#coding=utf-8
'''
Created on 2017年1月26日

@author: Administrator
'''

from selenium import webdriver
import os
import time

firefoxBin = os.path.abspath("C:\Program Files (x86)\Mozilla Firefox\firefox.exe")
os.environ["webdriver.firefox.bin"] = firefoxBin

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

driver.find_element_by_link_text("新闻").click()
time.sleep(3)

driver.quit()