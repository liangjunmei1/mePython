#encoding:utf-8
'''
Created on 2017-1-13

@author: Administrator
'''

class Bird():
    have_feather = True
    way_of_reproduction = 'egg'
    
    def move(self,dx,dy):
        position = [0,0]
        position[0] = dx
        position[1] = dy
        
        return position
    
summer = Bird()  # 创建一个对象
print summer.have_feather
print summer.move(3, 4)

# 类的继承直接在括号内写上该类名就行，空代表无继承，object表示该类没有父类
class Chicken(Bird):  
    move_way = 'fly'
    
summer  = Chicken()
print summer.move(5, 6)
