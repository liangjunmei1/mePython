#coding=utf-8
'''
Created on 2017年1月26日

@author: Administrator
'''
import os,time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

firefoxBin = os.path.abspath(r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe")
os.environ["webdriver.firefox.bin"] = firefoxBin

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").send_keys("selenium")

time.sleep(5)
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
time.sleep(5)
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')

time.sleep(5)
driver.find_element_by_id("kw").send_keys("selenium2")
time.sleep(5)
driver.find_element_by_id("su").send_keys(Keys.ENTER)

time.sleep(5)
driver.quit()
