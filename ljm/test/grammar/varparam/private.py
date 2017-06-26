#coding=utf-8
'''
Created on 2016-2-14

@author: ljm
'''
#默认情况下，类成员变量都是public，私有变量的定义是两个下划线 __，
#python 比较强调 public，private，中间变量的类型不是特别关注

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
