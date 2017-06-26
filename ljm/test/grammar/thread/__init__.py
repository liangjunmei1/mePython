#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Python 多线程和多进程

线程的状态：
new 创建
runnable 就绪，准备调度
running 运行
blocked 阻塞
dead 消灭

线程的类型：
主线程
子线程
守护线程(后台线程)
前台线程

python下多线程是鸡肋，推荐使用多进程
首先强调背景：
1、gil是什么？gil(global interpreter lock 全局解释器锁)，来源是python设计之初的考虑，为了数据安全所做的决定
2、每个cpu在同一时间只能执行一个线程(在单核cpu下的多线程其实都只是并发而不是并行，并发和并行在宏观上来讲都是同时处理
多路请求的概念，但并发和并行又有区别，并行是指两个或多个事件在同一时刻发生，而并发是指两个或者多个事件在同一时间间隔内发生)

在python多线程下，每个线程的执行方式：
1、获取gil
2、执行代码知道 sleep或者python虚拟机将其挂起
3、释放gil
可见，某个线程想要执行，必须先拿到 gil，我们可以把 gil看作是"通行证"，并且在一个python进程中，gil只有一个，拿不到通行证的线程，就不允许进去cpu执行
在Python2.x 里，gil的释放逻辑是当前线程遇到io操作或者ticks计数达到100(ticks可以看作是python自身的一个计数器，专门做用于gil，每次释放后归零，这个计数可以通过 sys.setcheckinterval来调整)，进行释放
而每次释放gil锁，线程进行锁竞争、切换线程、会消耗资源，并且由于gil锁存在，python 里一个进程永远只能同时执行一个线程(拿到gil的线程才能执行，这就是在多核cpu上，python的多线程效率并不高的原因)

在 unix/libux 下，可以使用 fork() 调用实现多进程
要实现跨平台的多进程，可以使用 multiprocessing模块
进程间通信是通过 queue、pipes 等实现的
"""
