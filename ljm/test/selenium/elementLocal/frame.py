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
url = 'file:///' + os.path.abspath('frame.html')
driver.get(url)

driver.implicitly_wait(2)
driver.switch_to_frame("f1")
driver.switch_to_frame("f2")

driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()

# driver.find_element_by_link_text("click")

driver.quit()


