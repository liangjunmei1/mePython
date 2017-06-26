#coding=utf-8
'''
Created on 2016-2-15

@author: ljm
'''
#python 可以强制抛出异常 raise

try:
    raise Exception("我是一个被强制抛出的异常!")
except Exception as e:
    print e
