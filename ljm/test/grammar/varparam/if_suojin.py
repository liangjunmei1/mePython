#encoding: utf-8
'''
Created on 2017-1-13

@author: Administrator
'''
x = 1
if x>1:
    print 'false'
elif x==1:
    print 'True'
else:
    print '条件都不成立时执行'

'''
if语法 后面跟冒号
if 条件1:
    内容
elif 条件2:
    内容
elif 条件3:
    内容
else:
    内容
'''

"""
in 判断 包含 contains
"""
str = "12345678xue54"
if '0' in str:
    print True
elif str.find("1") != -1:  # 找到 返回0 ，否则返回 -1
    print str.find("9")
else:
    print False