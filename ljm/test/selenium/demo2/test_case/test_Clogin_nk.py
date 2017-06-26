#coding:utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re, xlrd
from public import login

#此脚本将无效用例的多种情况集成在一个test方法中，可提高速度，但是报告
#只会生成一份，且中间若有失败用例，报告状态依然为pass，根据自己情况选择

class CLogin_nk(unittest.TestCase):

    def setUp(self):
        #调用浏览器
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(2)
        #最大化浏览器
        self.driver.maximize_window()
        
    #密码错误
    def test_login_nk(self):
        u"""iwebshop登录无效测试用例"""
        print u'test_login_nk开始执行'
        driver = self.driver
        wb = xlrd.open_workbook('C:\python\data\data.xls')
        sh = wb.sheet_by_name('lognk')

        username = sh.cell_value(1,0)
        password = sh.cell_value(1,1)
        driver.get("http://127.0.0.1:8888/iwebshop/")
        #调用登录函数
        login.login(self,username,password)
        
        #获取错误提示信息
        a = driver.find_element_by_class_name("prompt").text
        #print u'实际结果：',a
        
        b = u'用户名和密码不匹配'
        #print u'预期结果：',b
        c = cmp(a,b)
        if c == 0:
            print "success"
            print u'测试通过'
        else:
            print 'fail'
            print u'测试失败'

            

    #密码为空

        username = sh.cell_value(2,0)
        password = sh.cell_value(2,1)
        driver.get("http://127.0.0.1:8888/iwebshop/")
        #调用登录函数
        login.login(self,username,password)
        
        #获取错误提示信息
        a = driver.find_element_by_class_name("invalid-msg").text
        #print '实际结果：',a
        
        b = u'填写密码'
        #print u'预期结果：',b
        c = cmp(a,b)
        if c == 0:
            print "success"
            print u'测试通过'
        else:
            print 'fail'
            print u'测试失败'
            
    #用户名为空

        username = sh.cell_value(3,0)
        password = sh.cell_value(3,1)
        driver.get("http://127.0.0.1:8888/iwebshop/")
        #调用登录函数
        login.login(self,username,password)
        
        #获取错误提示信息
        a = driver.find_element_by_class_name("invalid-msg").text
        #print '实际结果：',a
        
        b = u'填写用户名或邮箱'
        #print u'预期结果：',b
        c = cmp(a,b)
        if c == 0:
            print "success"
            print u'测试通过'
        else:
            print 'fail'
            print u'测试失败'

    #用户名密码都为空

        username = sh.cell_value(4,0)
        password = sh.cell_value(4,1)
        driver.get("http://127.0.0.1:8888/iwebshop/")
        #调用登录函数
        login.login(self,username,password)
        
        #获取错误提示信息
        a = driver.find_element_by_class_name("invalid-msg").text
        #print '实际结果：',a
        
        b = u'填写用户名或邮箱'
        #print u'预期结果：',b
        c = cmp(a,b)
        if c == 0:
            print "success"
            print u'测试通过'
        else:
            print 'fail'
            print u'测试失败'

    #用户名不存在

        username = sh.cell_value(5,0)
        password = sh.cell_value(5,1)
        driver.get("http://127.0.0.1:8888/iwebshop/")
        #调用登录函数
        login.login(self,username,password)
        
        #获取错误提示信息
        a = driver.find_element_by_class_name("prompt").text
        #print u'实际结果：',a
        
        b = u'用户名和密码不匹配'
        #print u'预期结果：',b
        c = cmp(a,b)
        if c == 0:
            print "success"
            print u'测试通过'
        else:
            print 'fail'
            print u'测试失败'

            
    def tearDown(self):
        driver=self.driver
        driver.quit()


if __name__ == "__main__":
    unittest.main()

