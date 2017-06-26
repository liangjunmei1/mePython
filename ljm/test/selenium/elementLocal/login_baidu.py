#coding:utf-8
from selenium import webdriver


driver = webdriver.Firefox()                    #调用 webdriver 打开火狐
driver.maximize_window()                        #最大化浏览器

driver.get('https://www.baidu.com/')
            
driver.find_element_by_link_text("登录").click() 
driver.find_element_by_id("TANGRAM__PSP_8__userName").send_keys('ljm1227134894')
driver.find_element_by_id("TANGRAM__PSP_8__password").send_keys('liangjunmei')
driver.find_element_by_id("TANGRAM__PSP_8__submit").click()
            
