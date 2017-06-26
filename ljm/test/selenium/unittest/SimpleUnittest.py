#coding=utf-8
'''
Created on 2016-2-15

@author: ljm
'''

import unittest

class simpleunittest(unittest.TestCase):
    def test_add(self):
        self.assertEquals((1 + 2), 3);
        
if __name__ == "__main__":
    unittest.main
