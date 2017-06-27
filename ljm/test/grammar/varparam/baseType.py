#encoding: utf-8
'''
Created on 2017-1-13
@author: Administrator
'''
"""
 python 的变量不需要申明，可以直接使用
 print 后面可以打印出个内容，只直接用 , 隔开就行
 type() 是 python的内置函数，可以查看数据类型

 默认情况下，类成员变量都是public，私有变量的定义是两个下划线 __，
 python 比较强调 public，private，中间变量的类型不是特别关注
"""
class student:

    name = ""   #  public
    __age = 0    #  private
    _height = 0.0

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self._height = height

    def printinfo(self):
        print "I'm " + self.name + ", and age is " + str(self.age) + "."

s = student("ljm", 28, 160)
s.printinfo()

print (s.name)
#__age这个是不能执行的，私有变量不能直接调用,可以通过写方法来间接调用
print (s.__age)
#_height 是可以被调用的
print (s._height)


a = 10
print   10

print type(a)

a = 1.3
print (a,type(a))
print a,type(a)

a = True
a = False  # 注意大小写


