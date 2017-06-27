#coding=utf-8
'''
Created on 2016-2-15
@author: ljm
'''
try:
    1 / 0
except Exception as e:
    print "0不能被除"
else:
    print "没有异常"
finally:
    print "最后总是要执行我"
