# -*- coding: cp936 -*-
#coding = utf-8

import unittest


#定义测试文件查找目录
test_dir = 'C:\python'

#定义discover方法的参数
testlist= unittest.defaultTestLoader.discover(

        test_dir,
        pattern = 'test*.py',
        top_level_dir = None

        )
print testlist


if __name__ == '__main__':
    for i in testlist:
        print i
    runner = unittest.TextTestRunner()
    runner.run(testlist)
