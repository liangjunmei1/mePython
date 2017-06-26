# -*- coding: cp936 -*-
#coding = utf-8

import unittest


def createsuite():
    testunit = unittest.TestSuite()
    #定义测试文件查找目录
    test_dir = 'C:\python'

    #定义discover方法的参数
    discover = unittest.defaultTestLoader.discover(

        test_dir,
        pattern = 'test*.py',
        top_level_dir = None

        )
    print discover
    print '-------discover------0'
    #discover方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        print test_suite
        print '------testsuite--------1'
        for test_case in test_suite:
            print test_case
            print '------testcase-----2'
            testunit.addTests(test_case)
            print testunit
            print '------testunit-----3'
    return testunit

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(createsuite())

#discover()所返回的就是已经组装好测试用例的测试套件，我们没必要再将它通过 for 循环遍
#历出来添加到测试套件中。见all_test3.py
