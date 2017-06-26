#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
多进程并发
1、队列实现--使用 multiprocessing.JoinableQueue
"""

import  multiprocessing
import time
import random

class multiprocess():

    def read(q):
        while True:
            try:
                value = q.get()  #这是多进程并发的要点，q是一个JoinableQueue对象，支持get方法读取第一个元素，如果q中没有元素，进程就会阻塞，直至q中被存入新元素。
                print ('get %s from queeu.' % value)
                time.sleep(random.random())
            finally:
                q.task_done()

    def test(self):
        q = multiprocessing.JoinableQueue()
        pw1 = multiprocessing.Process(target=self.read(),args=(q,))
        pw2 = multiprocessing.Process(target=self.read(),args=(q,))

        pw1.daemon = True   #这两句话将子进程设置为守护进程——主进程结束后随之结束。
        pw2.daemon = True
        pw1.start()         #一旦运行到这两句话，子进程就开始独立于父进程运行了，它会在单独的进程里调用target引用的函数
        pw2.start()

        for c in [chr(ord('A')+i) for i in range(26)]:
            q.put(c)
        try:
            q.join()#这里指的就是任务是否执行完，如果没有，程序会阻塞住等待q中数据读完才开始继续执行
        except KeyboardInterrupt:
            print("stopped by hand")

if __name__ == '__main__':
    multiprocess().test()