# -*- coding: cp936 -*-
#coding = utf-8

import unittest, time, re
import HTMLTestRunner
import xlrd
import sys
#reload(sys)
#sys.setdefaultencoding('utf8')


def creatsuite():

    #1---�ҵ����е�test*py�ļ�
    testunit = unittest.TestSuite()
    #��������ļ�����Ŀ¼
    test_dir = 'c:\\python\\test_case'

    #����discover�����Ĳ���
    discover= unittest.defaultTestLoader.discover(

            test_dir,
            pattern = 'test*.py',
            top_level_dir = None

            )

    #2---discover����ɸѡ������������ѭ����ӵ������׼���
    for test_case in discover:
        print test_case
        testunit.addTests(test_case)
        
    return testunit


#3---���Ա���
now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))

#�����������·����֧�����·����
filename = "C:\\python\\report\\"+now+'result.html'
fp = file(filename, 'wb')
runner =HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title='iwebshop_test_report',
    description=u'test_case_description')



if __name__ == '__main__':
    #����creatsuite������������Ҫ��ӵ�test*.py�ļ���ɵĲ����׼�
    alltestnames = creatsuite()
    runner.run(alltestnames)
    fp.close()
