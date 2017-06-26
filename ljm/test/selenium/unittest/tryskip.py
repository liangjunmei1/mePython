#coding=utf-8
'''
Created on 2016-2-15

@author: ljm

可以使用unitest.skip装饰器族跳过test method或者test class,这些装饰器包括:
① @unittest.skip(reason):无条件跳过测试，reason描述为什么跳过测试
② @unittest.skipif(conditition,reason):condititon为true时跳过测试
③ @unittest.skipunless(condition,reason):condition不是true时跳过测试

'''
import unittest
import sys

class tryskip(unittest.TestCase):
    
    @unittest.skip("我就是要跳过你，没有原因...")
    def test_skipnoreason(self):
        print "我就是要跳过你，没有原因..."
        
    @unittest.skipIf("3.5" in sys.version, "执行") # python 版本是2.7
    def test_skipif(self):
        print "如果条件为真，我就跳过你..."
    
    @unittest.skipUnless(sys.platform.startswith("linux"), "执行") #系统是以win开头的
    def test_skipnnless(self):
        print "除非不满足该要求，否则跳过你"
        
    
if __name__ == "__main__":
    unittest.main()
