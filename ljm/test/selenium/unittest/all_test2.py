# -*- coding: cp936 -*-
#coding = utf-8

import unittest


def createsuite():
    testunit = unittest.TestSuite()
    #��������ļ�����Ŀ¼
    test_dir = 'C:\python'

    #����discover�����Ĳ���
    discover = unittest.defaultTestLoader.discover(

        test_dir,
        pattern = 'test*.py',
        top_level_dir = None

        )
    print discover
    print '-------discover------0'
    #discover����ɸѡ������������ѭ����ӵ������׼���
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

#discover()�����صľ����Ѿ���װ�ò��������Ĳ����׼�������û��Ҫ�ٽ���ͨ�� for ѭ����
#��������ӵ������׼��С���all_test3.py
