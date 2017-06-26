#coding=utf-8
'''
Created on 2016-2-14

@author: ljm
'''
#返回值，可以有多个
def returnValue():
    return 1, 2

res1, res2 = returnValue()
print (res1, res2)


list = []
list = returnValue()
print list
