#coding=utf-8
'''
Created on 2016-2-14

@author: ljm
'''
#默认参数
def personInfo(name="ljm",height=160,weight=50):
    print ("name = %s,height = %f cm,weight = %f kg"  %(name,height,weight))
    
personInfo()
personInfo("ljm2", 162)
personInfo("ljm3", 164,51)