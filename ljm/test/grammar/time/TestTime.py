#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
时间处理
"""

"""
time 类型
"""
import time
import calendar  #Calendar模块有很广泛的方法用来处理年历和月历

print time.localtime()
print time.strftime("%Y-%m-%d ",time.localtime())
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


print calendar.month(2017,6)




