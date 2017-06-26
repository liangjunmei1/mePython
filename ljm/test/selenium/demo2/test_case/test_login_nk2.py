#coding=gbk

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re, xlrd
from public import login

#�˽ű�����Ч�����Ķ���������ڶ��test�����У��ٶȱ�������Ϊÿ�ζ���Ҫ��������������Ǳ���
#�����ɶ�ݣ���ÿ�ݵ�״̬����������ִ��״̬����

class BLogin_nk(unittest.TestCase):

    def setUp(self):
        #���������
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(2)
        #��������
        self.driver.maximize_window()
        
    #�������
    def test_login_1(self):
        u"""iwebshop��¼��Ч��������"""
        print u'test_login_1��ʼִ��'
        driver = self.driver
        wb = xlrd.open_workbook('C:\python\data\data.xls')
        sh = wb.sheet_by_name('lognk')

        username = sh.cell_value(1,0)
        password = sh.cell_value(1,1)
        driver.get("http://127.0.0.1:8888/iwebshop/")
        #���õ�¼����
        login.login(self,username,password)
        
        #��ȡ������ʾ��Ϣ
        a = driver.find_element_by_class_name("prompt").text
        print u'ʵ�ʽ����',a
        
        b = u'�û��������벻ƥ��'
        print u'Ԥ�ڽ����',b
        c = cmp(a,b)
        if c == 0:
            print "success"
            print u'����ͨ��'
        else:
            print 'fail'
            print u'����ʧ��'

            

    #����Ϊ��
    #�������
    def test_login_2(self):
        u"""iwebshop��¼��Ч��������"""
        print u'test_login_2��ʼִ��'
        driver = self.driver
        wb = xlrd.open_workbook('C:\python\data\data.xls')
        sh = wb.sheet_by_name('lognk')
        username = sh.cell_value(2,0)
        password = sh.cell_value(2,1)
        driver.get("http://127.0.0.1:8888/iwebshop/")
        #���õ�¼����
        login.login(self,username,password)
        
        #��ȡ������ʾ��Ϣ
        a = driver.find_element_by_class_name("invalid-msg").text
        print u'ʵ�ʽ����',a
        
        b = u'��д����'
        print u'Ԥ�ڽ����',b
        c = cmp(a,b)
        if c == 0:
            print "success"
            print u'����ͨ��'
        else:
            print 'fail'
            print u'����ʧ��'
            
    #�û���Ϊ��
    #�������
    def test_login_3(self):
        u"""iwebshop��¼��Ч��������"""
        print u'test_login_3��ʼִ��'
        driver = self.driver
        wb = xlrd.open_workbook('C:\python\data\data.xls')
        sh = wb.sheet_by_name('lognk')
        username = sh.cell_value(3,0)
        password = sh.cell_value(3,1)
        driver.get("http://127.0.0.1:8888/iwebshop/")
        #���õ�¼����
        login.login(self,username,password)
        
        #��ȡ������ʾ��Ϣ
        a = driver.find_element_by_class_name("invalid-msg").text
        print u'ʵ�ʽ����',a
        
        b = u'��д�û���������'
        print u'Ԥ�ڽ����',b
        c = cmp(a,b)
        if c == 0:
            print "success"
            print u'����ͨ��'
        else:
            print 'fail'
            print u'����ʧ��'

    #�û������붼Ϊ��
    #�������
    def test_login_4(self):
        u"""iwebshop��¼��Ч��������"""
        print u'test_login_4��ʼִ��'
        driver = self.driver
        wb = xlrd.open_workbook('C:\python\data\data.xls')
        sh = wb.sheet_by_name('lognk')
        username = sh.cell_value(4,0)
        password = sh.cell_value(4,1)
        driver.get("http://127.0.0.1:8888/iwebshop/")
        #���õ�¼����
        login.login(self,username,password)
        
        #��ȡ������ʾ��Ϣ
        a = driver.find_element_by_class_name("invalid-msg").text
        print u'ʵ�ʽ����',a
        
        b = u'��д�û���������'
        print u'Ԥ�ڽ����',b
        c = cmp(a,b)
        if c == 0:
            print "success"
            print u'����ͨ��'
        else:
            print 'fail'
            print u'����ʧ��'

    #�û���������
    #�������
    def test_login_5(self):
        u"""iwebshop��¼��Ч��������"""
        print u'test_login_5��ʼִ��'
        driver = self.driver
        wb = xlrd.open_workbook('C:\python\data\data.xls')
        sh = wb.sheet_by_name('lognk')
        username = sh.cell_value(5,0)
        password = sh.cell_value(5,1)
        driver.get("http://127.0.0.1:8888/iwebshop/")
        #���õ�¼����
        login.login(self,username,password)
        
        #��ȡ������ʾ��Ϣ
        a = driver.find_element_by_class_name("prompt").text
        print u'ʵ�ʽ����',a
        
        b = u'�û��������벻ƥ��'
        print u'Ԥ�ڽ����',b
        c = cmp(a,b)
        if c == 0:
            print "success"
            print u'����ͨ��'
        else:
            print 'fail'
            print u'����ʧ��'

            
    def tearDown(self):
        driver=self.driver
        driver.quit()


if __name__ == "__main__":
    unittest.main()

