#coding=utf-8
'''
Created on 2017年1月26日

@author: Administrator
'''

from selenium import webdriver
import os,time
from selenium.webdriver.common.action_chains import ActionChains


firefoxBin = os.path.abspath(r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe")
os.environ["webdriver.firefox.bin"] = firefoxBin

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
driver.implicitly_wait(3)
# 获取设置按钮
m = driver.find_element_by_link_text("设置")
ActionChains(driver).click_and_hold(m).perform()

n = driver.find_element_by_link_text("搜索设置")
ActionChains(driver).click(n).perform()

select = driver.find_element_by_id("nr")
select.find_element_by_xpath("//option[@value='50']").click()

driver.find_element_by_xpath("/html/body/div[2]/div[7]/div/div/div/div/form/div/table/tbody/tr[7]/td[2]/div/a").click()
driver.switch_to_alert().accept()

driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
driver.find_element_by_id().clear()
driver.find_element_by_id().send_keys()

driver.quit()

