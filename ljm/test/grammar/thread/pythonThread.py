#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
python 提供了两个模块进行多线程的操作，分别是 thread和threading
前者四比较低级的模块，用于更底层的操作，一般应用级别的开发不常用
"""

import threading
import time

class pythonThread(threading.Thread):

    """
    第一种方法是 创建 threading.Thread 的子类，重写 run 方法
    """
    def run(self):
        for i in range(5):
            print 'thread{},@number:{}'.format(self.name,i)
            time.sleep(1)



