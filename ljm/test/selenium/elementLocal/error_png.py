#coding=utf-8
'''
Created on 2017年1月30日

@author: Administrator
'''

import os,time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

firefoxBin = os.path.abspath("C:\Program Files (x86)\Mozilla Firefox\firefox.exe")
os.environ["webdriver.firefox.bin"] = firefoxBin

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

try:
    driver.find_element_by_id("qqq")
except:
    driver.get_screenshot_as_file("D:\\ljm\\workSpacePython\\LearnPython\\src\\com\\yumimobi\\selenium\\error_png\\error.png")
finally:
    driver.quit()  

