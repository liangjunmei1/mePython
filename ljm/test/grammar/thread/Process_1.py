#coding:utf-8
'''
Python的标准库中的os模块包含普遍的操作系统功能。如果你希望你的程序能够与平台无关的话，这个模块是尤为重要的。
即它允许一个程序在编写后不需要任何改动，也不会发生任何问题，就可以在Linux和Windows下运行
    Python中的进程  os、subprocess、processing、multiprocessing
    
    语句pid=os.fork()，会为当前进程产生一个子进程并返回两个值，为父进程返回子进程的进程ID，为子进程返回0。
'''
import os

#os.fork()
os.system('pwd')


import subprocess
returnCode = subprocess.call('ls -l')
print returnCode