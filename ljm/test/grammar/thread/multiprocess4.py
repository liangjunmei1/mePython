#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
进程间通信
process直接肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信
python的multiprocess模块包装了底层的机制，提供了 queue、pipes等多重方式来交换数据

已queue为例,在父进程中创建两个子进程，一个向 queue写数据，一个从queue读数据
"""

from multiprocessing import Process,Queue
import os,time,random

"""写数据进程执行的代码"""
def write(q):
    for value in ['A','B','C','D','E','F']:
        print 'put %s to quequ...' % value
        q.put(value)
        time.sleep(random.random())

"""读数据进程执行的代码"""
def read(q):
    while True:
        value = q.get(True)
        print 'get %s from queue' % value


if __name__=="__main__":
    """父进程创建queue，并传递给各个子进程"""
    q = Queue()
    w1 = Process(target=write,args=(q,))
    # w2 = Process(target=write,args=(q,))
    r = Process(target=read,args=(q,))

    """启动子进程，写入"""
    w1.start()
    # w2.start()
    """启动子进程，读数据"""
    r.start()

    """等待write结果"""
    w1.join()
    # w2.join()
    """read这里是死循环，无法等待结果，只能强制终止"""
    r.terminate()
