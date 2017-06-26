#coding=utf-8

import unittest, time, re
import HTMLTestRunner
import xlrd
#把 test_case 目录添加到 path 下，这里用的相对路径
import sys

sys.path.append("\test_case")
#这里需要导入测试文件
from test_case import *
xlrd.Book.encoding = "gbk"
#打开excel文件
da = xlrd.open_workbook('C:\\python\\data\\test.xls','rb')
#获取一个工作表
table = da.sheets()[0]          #通过索引顺序获取



#获取行数
nrows = table.nrows
print nrows


testunit=unittest.TestSuite()

#循环读取Excel表格中的数据
for i in range(1,nrows):
    print 'ok'
    #获取filename的值
    cell_a = table.cell(i,0).value
    cell_a.encode('gbk')
    print cell_a
    print type(cell_a)
    #获取switch的值
    cell_b = table.cell(i,1).value
    print cell_b
    #eval(test)
    if cell_b==1.0:

        #将需要执行的测试用例加入到测试容器(套件)中
        testunit.addTest(unittest.makeSuite(eval(cell_a)))#将cell_a转换成类

'''
#执行测试套件
runner = unittest.TextTestRunner()
runner.run(testunit)
'''

#取前面时间
now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))

#定义个报告存放路径，支持相对路径。
filename = "C:\\python\\report\\"+now+'result.html'
fp = file(filename, 'wb')
runner =HTMLTestRunner.HTMLTestRunner(
stream=fp,
title=u'iwebshop测试报告',
description=u'用例执行情况：')

#执行测试用例
runner.run(testunit)
fp.close()
