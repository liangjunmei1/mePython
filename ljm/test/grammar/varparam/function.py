#encoding:utf-8
'''
Created on 2017-1-13

@author: Administrator
'''

# 指针传递
a = 1
def addFun(a):
    a = a+1
    return a
print addFun(a)
print a

#值 传递
b = [0,1,2,3,4]
def changeFun(a,b):
    a[0] = b;
    return a
print changeFun(b, 9)
print b


def runYear(year,month,day):
    if (year%4==0 and year%100!=0) or (year%400==0):
        return True
    else:
        return False
print runYear(2016, 11, 11)