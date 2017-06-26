#coding:utf-8

from selenium import webdriver
import os,time



driver = webdriver.Firefox()
driver.implicitly_wait(5)
driver.maximize_window()


file_path = 'file:///' + os.path.abspath('frame.html')
driver.get(file_path)

driver.switch_to_frame("if")

driver.find_element_by_id("word").send_keys("ipad")
driver.find_element_by_xpath("/html/body/div/div[3]/div[2]/form/input[2]").click()
time.sleep(5)

driver.switch_to_default_content()
driver.find_element_by_name("a").click()
time.sleep(5)
driver.quit()
