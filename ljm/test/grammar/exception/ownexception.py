#coding=utf-8
'''
Created on 2016-2-15

@author: ljm
'''
#python和其他语言一样，可以自定义自己的异常
#本例以输入一个字符串，判读字符串长度<6 就抛出异常为例
class ownInputEx(Exception):
    length = 0
    least = 0
    def __init__(self, length, least):
        self.length = length
        self.least = least
        
s = raw_input("请输入一个字符串...\n")
try:
    if len(s) < 6:
        raise ownInputEx(len(s), 6)
except ownInputEx as  x:
    print "实际长度 %d,最少长度%d" % (x.length, x.least)
else:
    print "没有异常"
finally:
    print "执行我"

        
