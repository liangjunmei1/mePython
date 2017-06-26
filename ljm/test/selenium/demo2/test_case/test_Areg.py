#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
import HTMLTestRunner,xlrd
from public import login



class AReg(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def test_reg(self):     
        
        u"""iwebshop注册测试用例"""      
        print u'test_reg开始执行'
        driver = self.driver
        wb = xlrd.open_workbook('C:\python\data\data.xls')
        sh = wb.sheet_by_name('reg')
        rows = sh.nrows
        for i in range(2,rows):
            email = sh.cell_value(i,0)
            username = sh.cell_value(i,1)
            password = sh.cell_value(i,2)
            repwd = sh.cell_value(i,3)
            driver.get("http://127.0.0.1:8888/iwebshop/")
            driver.implicitly_wait(8)
            time.sleep(1)
            #点击注册            
            driver.find_element_by_link_text(u"免费注册").click()
            driver.find_element_by_name("email").send_keys(email)
            driver.find_element_by_name("username").clear()
            driver.find_element_by_name("username").send_keys(username)
            driver.find_element_by_name("password").clear()
            driver.find_element_by_name("password").send_keys(password)
            driver.find_element_by_name("repassword").clear()
            driver.find_element_by_name("repassword").send_keys(repwd)
            driver.find_element_by_xpath(u"//input[@value='同意一下条款，提交']").click()

            #获取预期结果
            a = driver.find_element_by_xpath("//td/p[2]/span[@class='orange bold']").text
            print u'实际结果：',a
            #预期结果
            b = username
            print u'实际结果：',b
            #比对实际结果与预期结果
            try:
                #使用assertIn函数判断username是否在预期结果里面
                self.assertIn(username,a,msg = 'register failed!')
                print u'测试通过'
            except AssertionError,msg:
                #错误截图函数
                driver.get_screenshot_as_file('c:\python\error\reg_error.png')
                print msg
                print u'测试失败'

            time.sleep(1)
            #调用退出函数
            login.logout(self)
            

    def tearDown(self):
        driver = self.driver
        driver.quit()
        
if __name__ == "__main__":
    unittest.main()


