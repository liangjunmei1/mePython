#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
异常基类
@classmethod/@staticmethod
属于Python中常用的装饰器，被他们装饰的函数可以通过 类名称直接调用或者类实例调用

staticmethod: 只能操作static variables, 不能操作instance variables。如果操作 instance variables 写法如下：MeException.KeyError(MeException)
classmethod: 能访问类 变量，用法

@classmethod
    def IOError(cls,self):
        pass
调用:MeException.IOError(MeException)

或者：
@classmethod
    def IOError(self):
        pass
调用:MeException.IOError()
"""

class MeException(object):

    init = 3
    # def __init__(self):
    #     print "初始化..."

    @classmethod
    def IOError(cls,self):
        print cls.init,self.init,"我是一个 IOError 异常"

    @staticmethod
    def KeyError(self):
        print self.init,"我是一个 KeyError 异常"

if __name__=="__main__":
    MeException.IOError(MeException)
    # MeException.KeyError(MeException)
