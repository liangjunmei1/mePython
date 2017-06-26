#coding:utf-8
'''
Created on 2016-2-14

@author: ljm
'''

class student:
    '''  I is a 注释 '''
    name = ""
    age = 0
    scores = []
    def __init__(self):
        pass
    
    def setattr(self,name,age):
        self.name = name
        self.age = age
        
    def setscoures(self,scores):
        self.scores = scores
        
    def printinfo(self):
        print "Hello,I'm " + self.name + ",I'm "  + str(self.age) + "."
        print "My scores is : "
        for s in self.scores:
            print s 
            
s = student()
s.setattr("ljm",28)
s.setscoures([100,100])
s.printinfo()

#python 内置类属性
#__dict__：类的属性（包含一个字典，由类的数据属性组成）
#__doc__:类的文档字符串
#__name__:类名
#__module__:类定义所在的模块（类的全名是 ''__main__.className）,如果类位于一个导入模块mymod中，那么className.__module__等于mymod
# 三个单引号的注释是可以被打印出来的
print s.__doc__
#python 默认给每一个类都有一个字典
print s.__dict__
print s.__module__