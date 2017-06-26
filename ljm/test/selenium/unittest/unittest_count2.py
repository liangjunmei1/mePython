# -*- coding: cp936 -*-
#coding = utf-8

from count import Count
import unittest

class TestCount(unittest.TestCase):

    def setUp(self):
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
        
    def tearDown(self):
        pass


class TestSubtraction(unittest.TestCase):

    def setUp(self):
        pass


    def test_sub(self):
        self.j = Count(2,3)
        self.sub = self.j.sub()
        self.assertEqual(self.sub,-1)

    def test_sub2(self):
        self.j = Count(2.5,1.5)
        self.sub = self.j.sub()
        self.assertEqual(self.sub,1.0)

    def tearDown(self):
        pass



if  __name__ == '__main__':
    
    #������Լ�

    suite = unittest.TestSuite()                #ʵ����Testsuite��
    suite.addTest(TestCount('test_add'))        #����TestSuite���е�addTest����
    suite.addTest(TestCount('test_add2'))
    suite.addTest(TestCount('test_add3'))
    suite.addTest(TestSubtraction('test_sub'))
    suite.addTest(TestSubtraction('test_sub2'))
    #ִ�в���

    runner = unittest.TextTestRunner()      #ʵ����TextTestRunner��
    runner.run(suite)                       #����Testsuite���е�addTest����
