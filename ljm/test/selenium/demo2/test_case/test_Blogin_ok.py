#coding=gbk

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re, xlrd
from public import login




class BLogin_ok(unittest.TestCase):

    def setUp(self):

        #调用浏览器
        self.driver=webdriver.Firefox()
        
        self.driver.implicitly_wait(3)
        #最大化浏览器
        self.driver.maximize_window()

    def test_login_ok(self):
        u"""iwebshop登录有效测试用例"""
        print u'test_login_ok 开始执行'
        driver = self.driver
        wb = xlrd.open_workbook('C:\python\data\data.xls')
        sh = wb.sheet_by_name('logok')
        rows = sh.nrows
        for i in range(1,rows):
            username = sh.cell_value(i,0)
            password = sh.cell_value(i,1)
            #访问网址
            driver.get("http://127.0.0.1:8888/iwebshop/")
            
            #调用登录函数
            login.login(self,username,password)

            #获取错误提示信息
            a=driver.find_element_by_class_name("loginfo").text

            #print repr(text)
            #a= text.encode('gb2312')

            #print '实际结果：',a
            b=username+u"您好，欢迎您来到iwebshop购物！[安全退出]"
            #print '预期结果：',b
            c=cmp(a,b)
            if c==0:
                print "success"
                print u'测试通过'
            else:
                print "fail"
                #print u'测试失败'


            #调用退出函数
            login.logout(self)

    def tearDown(self):
        driver=self.driver
        driver.quit()


if __name__ == "__main__":
    unittest.main()

