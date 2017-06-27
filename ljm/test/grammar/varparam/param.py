#encoding: utf-8
'''
Created on 2017-1-13
@author: Administrator
'''
#参数传递顺序： 先位置，在关键字，在包裹，在包裹关键字
'''
根据位置传递
'''
def f(a,b,c):
    return a+b+c
#print f(1,2,3)

'''
关键字传递：关键字传递是根据每个参数的名字进行传递
'''
#print f(a=1,b=2,c=3)

'''
关键字和位置传递混用，但位置参数要出现在关键字参数之前
'''
#print f(1,b=2,c=3)

'''
参数默认值
'''
def f2(a,b,c=4):
    print a,b,c

f2(1,2)
f2(1,2,3)

'''
包裹传递：
在定义函数时，我们有时候并不知道调用的时候会传递多少个参数，这时候，包裹(packing)未知参数，或者包裹关键字参数，来进行参数传递，会非常有用
'''
#包裹位置传递:在func参数表中，所有的参数被name收集，根据位置合并一个元祖（tuple）
def func(*name):
    print type(name)
    print name

func(1,2,3)
func(1,2,3,4,5,6)

#关键字传递: dict 是一个字典，收集所有的关键字，传递给函数 func，为了提醒python，参数dict是包裹关键字传递所用的字典，在dict前面加 **
def func2(**dict):
    print type(dict)
    print dict

func2(a=1,b=2,c=3)
func2(a=1,b=2)

'''
*和** 也可以在调用的时候使用，即 解包裹(unpacking)
'''
def func3(a,b,c):
    print a,b,c

args = (1,2,3)
func3(*args)

dict = {'a':1,'b':2,'c':3}
func3(**dict)