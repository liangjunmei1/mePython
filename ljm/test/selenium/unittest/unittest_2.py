#coding = utf-8

from count import Count

import unittest

class TestCount(unittest.TestCase):

    def setup(self):
        self.j = Count(2,3)


    def test_add(self):
        self.add = Count(2,3).add()
        self.assertEqual(self.add,5)
        
    def teardown(self):
        pass

if  __name__ == '__main__':
    
    #构造测试集

    suite = unittest.TestSuite()            #实例化Testsuite类
    suite.addTest(TestCount('test_add'))    #调用TestSuite类中的addTest方法

    #执行测试

    runner = unittest.TextTestRunner()      #实例化TextTestRunner类
    runner.run(suite)                       #调用Testsuite类中的addTest方法
