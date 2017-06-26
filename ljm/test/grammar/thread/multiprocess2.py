#!/usr/bin/python
# -*- coding: utf-8 -*-

from multiprocessing import Process
import os
import time

# 子进程要执行的代码
def run_proc(name):
    """
    子进程永远返回0，父进程返回子进程的id
    一个父进程可以fork出很多子进程，所以，父进程需要记下每个子进程的id
    子进程只需要调用 getppid()就可以得到父进程的id
    :param name:
    :return:
    """
    time.sleep(10)
    print 'Run child process %s (%s)...' % (name, os.getpid())

if __name__=='__main__':
    """
    getpid() 得到当前进程id
    """
    print 'Parent process %s.' % os.getpid()
    """
    创建子进程时只需要传入一个执行函数和函数的参数，创建一个 process实例
    start() 启动一个进程
    join() 可以等待子进程结束后在继续往下运行，通常用于进程间的同步
    """
    p1 = Process(target=run_proc, args=('test1',))
    p2 = Process(target=run_proc, args=('test2',))
    print 'Process will start.'
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print 'Process end.'
