#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
异常语法
"""
try:
    raise IOError("抛出异常")
except IOError as io:
    print "".format(io)
except RuntimeError as run:
    print "".format(run)
else: #没有异常时必须执行的语句，可以保护代码会遇到一些不可预测的异常
    print "no exception"
finally:
    print "1"


"""
自定义异常:可以向正常的类一样处理一些问题
"""
class myRuntimeError(Exception):

    def __init__(self,value):
        self.value = value

    def __str__(self):
        return repr(self.value)  # 返回对象的标准字符串表现形式
try:
    raise myRuntimeError(1*2)
except Exception as a:
    print a


