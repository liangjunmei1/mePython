#coding=utf-8
'''
Created on 2017年1月26日

@author: Administrator
'''
import os,time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

firefoxBin = os.path.abspath("C:\Program Files (x86)\Mozilla Firefox\firefox.exe")
os.environ["webdriver.firefox.bin"] = firefoxBin

driver = webdriver.Firefox()
url = 'file:///' + os.path.abspath('upload_file.html')
driver.get(url)

driver.find_element_by_name("file").send_keys("D:\ljm\workSpacePython\LearnPython\src\com\yumimobi\selenium\locateElement\upload_file.html")
time.sleep(2)

driver.quit()

