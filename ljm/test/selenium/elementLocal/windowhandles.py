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

nowHandle = driver.current_window_handle()
allHandle = driver.window_handles()

for handle in allHandle:
    if handle!=nowHandle:
        driver.switch_to_window(handle)
        #操作

driver.switch_to_window(nowHandle)
