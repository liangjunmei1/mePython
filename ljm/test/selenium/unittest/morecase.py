#coding=utf-8
'''
Created on 2016-2-15

@author: ljm
'''
import unittest
class morecase(unittest.TestCase):
    #必须以test开头
    def test_add(self):
        self.assertEqual(1, 1)
        
    def test_strcmp(self):
        s = "hello world"
        self.assertEqual(s.split(), ["hello", "world"])
        
if __name__ == "__main__":
    unittest.main()
