#encoding: utf-8
'''
Created on 2017年1月14日

@author: Administrator
'''
'''
在python中，for循环后的in跟随一个序列的话，循环每次使用的序列元素，而不是序列的下标
'''
s = 'qazxswedcvfr'
for i in range(0,len(s),2):
    print s[i]

'''
enumerate() :在每次循环中，可以同时得到下标和元素
            实际上，enumerate(),在每次循环中返回的是包含每个元素的定值表，两个元素分别赋值 index，char
'''
for (index,char) in enumerate(s):
    print index,char
    
'''
如果有多个等长的序列，然后想要每次循环时从各个序列分别取出一个元素，可以利用 zip() 来实现
'''    
ta = [1,2,3]
tb = [4,5,6]
tc = ['a','b','c']
for (a,b,c) in zip(ta,tb,tc):
    print (a,b,c)
    

ta = [1,2]
tb = [3,4]

zip1 = zip(ta,tb)
print zip1

na,nb = zip(*zip1)
print na,nb
