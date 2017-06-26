#coding:utf-8

class interface(object): 
    def f1(self,a): 
        pass 
    
class I1(interface): 
    def f1(self,a): 
        return a+1 

class I2(interface): 
    def f1(self,a): 
        return a-1 
    
'''I1,I2 分别对接口 interface 有不同的实现'''
a=I1() 
b=I2() 
c=[a,b] 
for i in c: 
    print i.f1(1)