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

        #���������
        self.driver=webdriver.Firefox()
        
        self.driver.implicitly_wait(3)
        #��������
        self.driver.maximize_window()

    def test_login_ok(self):
        u"""iwebshop��¼��Ч��������"""
        print u'test_login_ok ��ʼִ��'
        driver = self.driver
        wb = xlrd.open_workbook('C:\python\data\data.xls')
        sh = wb.sheet_by_name('logok')
        rows = sh.nrows
        for i in range(1,rows):
            username = sh.cell_value(i,0)
            password = sh.cell_value(i,1)
            #������ַ
            driver.get("http://127.0.0.1:8888/iwebshop/")
            
            #���õ�¼����
            login.login(self,username,password)

            #��ȡ������ʾ��Ϣ
            a=driver.find_element_by_class_name("loginfo").text

            #print repr(text)
            #a= text.encode('gb2312')

            #print 'ʵ�ʽ����',a
            b=username+u"���ã���ӭ������iwebshop���[��ȫ�˳�]"
            #print 'Ԥ�ڽ����',b
            c=cmp(a,b)
            if c==0:
                print "success"
                print u'����ͨ��'
            else:
                print "fail"
                #print u'����ʧ��'


            #�����˳�����
            login.logout(self)

    def tearDown(self):
        driver=self.driver
        driver.quit()


if __name__ == "__main__":
    unittest.main()

