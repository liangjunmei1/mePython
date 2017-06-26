#coding=utf-8
'''
Created on 2016-2-14

@author: ljm
'''
#可变参数,后面的 * 就是通配符的意思，能够匹配我们的参数个数
#比如 ？代表至少一个， * 0个或者没有
def varFun(var1,*values):
    print ("the first parameter is : "  + var1)
    
    for var in values:
        print var

varFun(str(1))
varFun(str(1),100,200,300,400,500)
