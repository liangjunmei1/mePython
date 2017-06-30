#encoding: utf-8
'''
Created on 2017-1-13
@author: Administrator
'''

"""
sequence（序列）是一组有顺序的对象的集合
序列可以包含一个或多个元素，也可以没有元素
序列里面可以包含 基本数据类，也可以包含另一个序列

序列有两种： tuple(定值表：元祖)  list(表)
tuple和 list的区别在于  tuple一旦建立，各个元素不可在变更，而list的元素可以在变更
"""
s1 = (1,3,8,2.4,'love',1,False)  # tuple
s2 = [True,5,'simple']     # list

# for temp in s1:     #直接循环 s1 中的元素
#     print temp
#
# print s1.__contains__(3)
# for temp in range(0,s1.__len__()):  #通过下标得到 s1 中元素的值
#     print s1[temp],temp

# for index,value in enumerate(s1):     # 利用 enumerate() 函数 同时得到下标和值
#     print "index=",index,"value=",value
#     print "index=%s  value=%s" % (index,value)
# print type(s1),s1
# print type(s2),s2

# s3 = [1,[2,3,4]]
# s4 = ()
#
# print s3,s4

# s5 = (1,s1) # 元素的引用  从 0 开始
# print s5[0]
# print s5[1][0]  # 相当于先取到s3的下标为1的元素 a，在从a中取它下标为0的元素
#
# s5[0] = 2   # tuple的元素不可变更，该操作会报错
# s3[0] = 2
# print s3,s5
# print s1[0:2:1]   # 上限不包括在内 # 其他引用方式  范围引用： 基本样式[下限：上限：步长]
# print s1[-1] # 尾部引用
# str = 'abcdefg'  # 字符串是一种 特殊的元祖（tuple）
# print str[0:3]
# print type(str[0]) #str[0] = 'A'
# print str[6:0:-1]

"""join"""
# str = ['1','2','3']
# str = ('1','2','3')
str = {'1':11 ,'2':22,'3':33}
print type("".join(str)),"".join(str)