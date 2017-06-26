#coding=utf-8
'''
Created on 2016-2-15

@author: ljm
'''
import unittest
import random

#python 会在每个用例的前后执行一遍 setUp，tearDown，对于每一个用例都是分别来处理的。
class trysetupteardown(unittest.TestCase):
    
    def setUp(self):
        self.intarr = [1, 2, 3, 4]
        self.strcmp = "hello world"
        self.strarr = ["hello", "world"]
        print "setup"
        
    def tearDown(self):
        del self.strcmp
        self.strarr = None
        print "teardown"
        
    def test_intarr(self):
        self.assertIn(random.choice(self.intarr), self.intarr)
        
    def test_strcmp(self):
        self.assertEqual(self.strcmp.split(), self.strarr)
    
if __name__ == "__main__":
    unittest.main()
        
        
    
