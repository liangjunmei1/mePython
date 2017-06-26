#coding=utf-8
'''
Created on 2017年1月26日

@author: Administrator
'''

from selenium import webdriver
import os


firefoxBin = os.path.abspath(r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe")
os.environ["webdriver.firefox.bin"] = firefoxBin

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

# 获取百度输入框的方式
driver.find_element_by_id("kw").send_keys(u"通过id定位")
driver.find_element_by_name("wd").send_keys(u"通过name定位")
driver.find_element_by_class_name("s_ipt").send_keys(u"通过classname定位")


driver.find_element_by_id("su").click()
driver.quit()