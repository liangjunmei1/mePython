#coding:utf-8
'''
pyhton的数据类型  int float str
Python自动识别数据类型，定义变量不需要书写类型
'''

a=4
b=2.5
m='hello,python'
m2='m'
m3="let's go "
#print 'result is :',a
#print type(a),type(b),type(m),type(m2),type(m3)
#l = raw_input("请输入数值:")
#print type(l)
#print 'result is:',l

'''列表的定义方式'''
s1 = [1,2.5,'go'] 
'''tuple 序列的定义方式'''
s2 = (1,2.5,'go')
#print s1
#print s2

#上限默认不打印，下限 代表起始位置s3[1]=2,从2开始，步长 代表 下一元素的增量,步长 =1，可以省略或两个元素之间逗号的个数
s3 = [0,1,6,3,4,5,9,7,8,2]
s4 = (0,1,2,3,4,5,6,7,8,9)
#print s3[3:8:2],s3[9]
#倒数的元素可用负数表示 ,比如: -1 代表最后一个元素
#print s3[-1]
#s3.reverse()
#s3.sort()
#print s3
#print sorted(s3)
#print s3
#print max(s3)
#print min(s3)
#print len(s3)
#删除第三个位置上的元素
#del s3[3]
#print s3
s3.append(90)
#s4.index(0,8 )
#print s3
#print s4

#字典 无顺序可言
w = {'a':1,'b':11,'c':111}
print w.keys()
print w.values()
print w.items()
del w['a']
print w
print w.get('a')
#print w['c']
#w.clear()
print w
#d 在字典内存在就修改它的值，不存在，就添加 d的值等于20
w['d'] = 20
#print w

#字符串的加就是连接，不同的数据类型是不能做加法的
a="123"
b="321"
print a+b