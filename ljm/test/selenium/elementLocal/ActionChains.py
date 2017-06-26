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
driver.get("http://www.baidu.com")

ActionChains(driver).click_and_hold(driver.find_element_by_link_text("设置")).perform()
ActionChains(driver).double_click(driver.find_element_by_xpath("/html/body/div[2]/div[6]/a")).perform()

time.sleep(5)
driver.quit()