#encoding: utf-8
'''
Created on 2017-1-13
@author: Administrator
'''

'''
    内置函数： dir()、help()
    dir(): 用来查询一个类或者对象所有的属性
    help():用来查询的说明文档
'''

#print dir(list)
#print help(list)
#print type(list)

n1 = [1,2,3,3,34,56,7,8,9,0]
print n1.count(3)       #统计n1中有多少个数字3
print n1.index(3)       #查询 n1 中第一个3的下标
n1.append('00')
n1.sort()
print n1.pop()
n1.remove(3)
n1.insert(0, 99)
print n1

print "元素个数",len(n1)

print [1,2,3]+[4,5]

class superList(list):
    def __sub__(self,b):
        a = self[:]
        b = b[:]
        while len(b)>0:
            element_b = b.pop()
            if element_b in a:
                a.remove(element_b)
        return a

print superList([1,2,3]) - superList([1,2])