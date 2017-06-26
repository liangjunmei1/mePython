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
