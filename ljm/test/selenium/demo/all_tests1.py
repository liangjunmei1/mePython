#coding=utf-8
import unittest,time
import HTMLTestRunner
#把 test_case 目录添加到 path 下，这里用的相对路径
import sys
sys.path.append("\test_case")
#这里需要导入测试文件
from test_case.public.reg import reg
from test_case.public.login_1 import login

testunit=unittest.TestSuite()

#将测试用例加入到测试容器(套件)中
testunit.addTest(unittest.makeSuite(reg))
testunit.addTest(unittest.makeSuite(login))
'''
#执行测试套件
runner = unittest.TextTestRunner()
runner.run(testunit)
'''

#取前面时间
now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))

#定义个报告存放路径，支持相对路径。
filename = "C:\\"+now+'result.html'
fp = file(filename, 'wb')
runner =HTMLTestRunner.HTMLTestRunner(
stream=fp,
title=u'iwebshop测试报告',
description=u'用例执行情况：')

#执行测试用例
runner.run(testunit)
fp.close()
