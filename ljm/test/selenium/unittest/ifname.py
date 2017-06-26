#coding=utf-8
'''
Created on 2016-2-15

@author: ljm
'''
def fun1():
    print (__name__)
    
class fun2():
    def __init__(self):
        print(__name__)
        
fun1()
print ("================")
fun2()

#__name__我自己本类中运行，代表的是 __main__
# 如果我在别的文件中引用了 ifname 类，那么 __name__ 代表的就是 ifname 的类名称
#代表的是不是我自己在运行
if __name__ == " __main__":
        pass
    
