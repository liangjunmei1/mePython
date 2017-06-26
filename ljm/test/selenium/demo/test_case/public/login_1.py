#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class login(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_login(self):
        
        u"""iwebshop登录测试用例"""
        
        driver = self.driver
        driver.get("http://localhost:8013/iwebshop/")
        driver.maximize_window()
        driver.find_element_by_link_text(unicode('登录',"UTF-8")).click()
        self.driver.implicitly_wait(10)
        driver.find_element_by_name("login_info").send_keys('r001')
        driver.find_element_by_name("password").send_keys('111111')
        time.sleep(1)
        driver.find_element_by_class_name("submit_login").click()
        #print driver.title
        #使用try---except接收抛出的错误
        try:
            result=driver.find_element_by_class_name("loginfo").text
            #print result
            ex_result=unicode("r002您好，欢迎您来到iwebshop购物！[安全退出]","UTF-8")
            #使用try---except接收抛出的错误
        
            #如果比对失败，msg定义错误输出内容，执行except的错误处理
            self.assertEqual(ex_result,result,msg='login failed!'),
            
        except AssertionError,msg:
            driver.get_screenshot_as_file("C:/python/erro_png/error1_png.png")
            print msg
        except:
            #截取当前错误页面
            driver.get_screenshot_as_file("C:/python/erro_png/error2_png.png")
        driver.quit()
        print "login pass"
        
    def tearDown(self):
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
