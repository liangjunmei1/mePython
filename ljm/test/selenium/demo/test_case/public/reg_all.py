#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
import HTMLTestRunner

class reg(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_reg(self):        
        # self.driver = webdriver.Firefox()
        driver = self.driver
        driver.get("http://localhost:8013/iwebshop/")
        #time.sleep(1)
        driver.maximize_window()
        driver.find_element_by_class_name("reg").click()            
        self.driver.implicitly_wait(3)
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys('a001@136.com')
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys('a001')
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys('111111')
        driver.find_element_by_name("repassword").clear()
        driver.find_element_by_name("repassword").send_keys('111111')
        driver.find_element_by_xpath(u"//input[@value='同意一下条款，提交']").click()
        # alert=driver.switch_to_alert()
        # alert.accept()
        # print alert.text()
        time.sleep(1)
        driver.quit()
    
    def test_search(self):
        # self.driver = webdriver.Firefox()
        driver = self.driver
        driver.get("http://localhost:8013/iwebshop/")
        #time.sleep(1)
        driver.maximize_window()
        driver.quit()
        

    def tearDown(self):
        driver = self.driver
        self.assertEqual([], self.verificationErrors)
        driver.quit()
        
if __name__ == "__main__":
    
    #定义一个单元测试容器
    testunit=unittest.TestSuite()
    #将测试用例加入到测试容器中
    testunit.addTest(reg("test_reg"))
    testunit.addTest(reg("test_search"))
    
    #定义个报告存放路径，支持相对路径
    filename = 'C:\\python\\report\\result.html'
    fp = file(filename, 'wb')
    #定义测试报告
    runner =HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u'iwebshop测试报告',
    description=u'用例执行情况：')
    #运行测试用例
    runner.run(testunit)
    fp.close() #关闭报告文件
    
