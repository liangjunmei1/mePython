#coding:utf-8
'''
    函数： def add是自己随意写的函数名
  调用：add()
  如果有返回值的话，需要接受返回值
''' 
def add(a,b):
    print a+b

add(2,3)

def add1(a,b):
    return a+b

d = add1(5,3)
print d