#coding:utf-8
'''
类：具有相同特性，且能够完成某些动作的对象组成的一个集合
属性：类中的事物所具有的特性，趋于静态
方法：类中的事物所能够完成的功能，趋于动态
对象：类中的某一个具体的事物
实例化：找对象的过程

self: 是python中默认添加的第一个参数,必须有
__init__: python 内置的方法，不写照样会调用,brand 是python内置方法的参数，所以是类的参数
''' 
class Calc(object):
    def __init__(self,brand):
        self.brand=brand
    def add(self,a,b):
        print a+b

p = Calc('tom')  #实例化Calc类，找对象，调用Calc 需要传参数，是因为有brand，跟object没有关系
p.add(1, 2)

class Calc2(object):
    def add(self,a,b):
        print a+b

p = Calc2()
p.add(1, 2)
'''
继承，继承谁就直接写谁就行
class Calc_1(Calc2)：
代表Calc_1 继承了 Calc2
'''
#class Calc_1(Calc2):