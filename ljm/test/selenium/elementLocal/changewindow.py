#coding=utf-8
'''
Created on 2016-2-16

@author: ljm
'''
from selenium import  webdriver
import time

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(3)
driver.get("http://www.baidu.com")

#获得百度搜索窗口句柄
sreach_windows = driver.current_window_handle
print "当前窗口的是: ", sreach_windows

#driver.find_element_by_link_text(u'登录').click()
#driver.find_element_by_link_text(u"立即注册").click()


#获得当前所有打开的窗口的句柄
all_handles = driver.window_handles
#进入注册窗口
for handle in all_handles:
    print "每个窗口是: ", handle
    if handle != sreach_windows:
        driver.switch_to_window(handle)
        print 'now register window!'
        driver.find_element_by_name("userName").send_keys('username')
        driver.find_element_by_name('password').send_keys('password')
#……
    
#进入搜索窗口
for handle in all_handles:
    if handle == sreach_windows:
        driver.switch_to_window(handle)
        print 'now sreach window!'
        #driver.find_element_by_id('TANGRAM__PSP_2__closeBtn').click()
        driver.find_element_by_id("kw").send_keys("selenium")
        driver.find_element_by_id("su").click()
    
time.sleep(5)
driver.quit()
