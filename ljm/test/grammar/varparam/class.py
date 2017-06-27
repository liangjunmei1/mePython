#encoding:utf-8
'''
Created on 2017-1-13
@author: Administrator
'''

"""
创建类 Bird()
类的继承直接在括号内写上该类名就行，空代表无继承，object表示该类没有父类 Chicken(Bird)
"""
"""
__init__():在创建对象时自动执行
类似 java的构造函数，也即是我在创建对象的时候，给构造函数传参数
"""

class Bird():
    have_feather = True
    way_of_reproduction = 'egg'

    def __init__(self):
        pass

    def move(self,dx,dy):
        position = [0,0]
        position[0] = dx
        position[1] = dy

        return position

        #默认参数
    def personInfo(name="ljm",height=160,weight=50):
        print ("name = %s,height = %f cm,weight = %f kg"  %(name,height,weight))

        #参数无关性,也就是参数的顺序可以改变，但是调用的时候需要加上参数的名称
    def personInfo2(name,height,weight):
         print ("name = %s,height = %f,weight = %f" %(name,height,weight))


summer = Bird()  # 创建一个对象
print summer.have_feather
print summer.move(3, 4)

summer.personInfo("ljm",160, 50)
summer.personInfo(name="ljm",  weight=50,height=160)


class Chicken(Bird):
    move_way = 'fly'

summer  = Chicken()
print summer.move(5, 6)

"""默认参数"""
Bird().personInfo()
Bird().personInfo("ljm2", 162)
Bird().personInfo("ljm3", 164,51)
