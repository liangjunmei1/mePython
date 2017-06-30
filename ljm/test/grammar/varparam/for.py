#encoding: utf-8
'''
Created on 2017-1-13
@author: Administrator
'''
'''
语法
for 元素 in 序列:
    内容
s = [1,2,3,4,5]
a = 1
for a in s:  # 从s中取值之后赋值给 a
    print a

# range 的功能是新建一个表，表中的元素从0开始，
# range(4) 从0开始，创建4个值
idx = range(4)
print idx
for a in range(10):
    print a
'''
'''
语法： while 条件:
        内容
i = 1
while i<10:
    print i
    i = i+1
'''
# 中断循环 continue，break
# continue 在循环的一次执行中，如果遇到continue，跳过这一次执行，进行下一次操作
# break # 停止执行整个循环
i=0
for i in range(4):
    if i==2:
        continue
    print i

for i in range(4):
    if i==2:
        break
    print i

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
    print "index=%s ,char=%s" % (index,char)

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
