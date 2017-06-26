#encoding: utf-8
'''
Created on 2017-1-13

@author: Administrator
'''

class Human():
#    def __init__(self,input_gener):
#        self.gender = input_gener
#        print self.gender
    def __init__(self):
        self.gender = 'qq'
        print self.gender
        
#lili = Human('qq')
lili = Human()

print dir(Human())
print help(Human())
# __init__():在创建对象时自动执行
# 类似 java的构造函数，也即是我在创建对象的时候，给构造函数传参数
        