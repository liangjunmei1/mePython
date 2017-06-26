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
url = 'file:///' + os.path.abspath('checkbox.html')
driver.get(url)

# inputs = driver.find_elements_by_tag_name("input")
# for input in inputs:
#     if input.get_attribute('type') == 'checkbox':
#         input.click()

#第二种方式
checkboxs = driver.find_elements_by_css_selector("input[type=checkbox]")
print len(checkboxs)
for checkbox in checkboxs:
    checkbox.click()
    
checkboxs2 = driver.find_elements_by_css_selector("input[type=checkbox]")
checkboxs2.pop().click()

time.sleep(2)
driver.quit()