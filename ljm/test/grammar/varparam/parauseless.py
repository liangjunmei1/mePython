#coding=utf-8
'''
Created on 2016-2-14

@author: ljm
'''
#参数无关性,也就是参数的顺序可以改变，但是调用的时候需要加上参数的名称
def personInfo(name,height,weight):
    print ("name = %s,height = %f,weight = %f" %(name,height,weight))
    
personInfo("ljm",160, 50)

personInfo(name="ljm",  weight=50,height=160)