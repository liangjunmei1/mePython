# -*- coding: cp936 -*-
#coding = utf-8

import unittest


#��������ļ�����Ŀ¼
test_dir = 'C:\python'

#����discover�����Ĳ���
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
