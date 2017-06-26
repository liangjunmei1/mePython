#coding=utf-8
'''
Created on 2016-2-14

@author: ljm
'''

class tryDestruct:
    
    def __init__(self):
        print "我是初始化..."
        
    def __del__(self):
        print "我是删除..."
        
    def printinfo(self):
        print "我什么都不做..."
        
t = tryDestruct()
del t  #python 和Java一样，是可以进行垃圾回收的，当一个类不在被调用的时候，python就会自动对其进行回收
t.printinfo()

