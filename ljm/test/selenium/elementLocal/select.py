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
url = 'file:///' + os.path.abspath('drop_down.html')
driver.get(url)

selects = driver.find_element_by_id("ShippingMethod")
# selects.find_element_by_xpath("//option[@value='10.69']").click()

options = driver.find_elements_by_tag_name("option")
time.sleep(3)
for option in options:
    value = option.get_attribute("value")
    print type(value)
    if (option.get_attribute("value")==u'10.69'):
        time.sleep(2)
        option.click()

time.sleep(3)
driver.quit()