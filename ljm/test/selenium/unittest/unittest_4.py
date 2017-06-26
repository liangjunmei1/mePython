# -*- coding: cp936 -*-
#coding = utf-8

from count import Count
import unittest

class TestCount(unittest.TestCase):

    def setup(self):
        pass


    def test_add(self):
        self.j = Count(2,3)
        self.add = self.j.add()
        self.assertEqual(self.add,5)

    def test_add2(self):
        self.j = Count(2.5,3.5)
        self.add = self.j.add()
        self.assertEqual(self.add,6.0)

    def test_add3(self):
        self.j = Count('hello','world')
        self.add = self.j.add()
        self.assertEqual(self.add,'helloworld')
        
    def teardown(self):
        pass

if  __name__ == '__main__':
    #������Լ�

    suite = unittest.TestSuite()            #ʵ����Testsuite��
    suite.addTest(TestCount('test_add'))    #����TestSuite���е�addTest����
    suite.addTest(TestCount('test_add2'))
    suite.addTest(TestCount('test_add3'))
    #ִ�в���

    runner = unittest.TextTestRunner()      #ʵ����TextTestRunner��
    runner.run(suite)                       #����Testsuite���е�addTest����
