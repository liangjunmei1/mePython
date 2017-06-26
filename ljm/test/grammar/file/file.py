#encoding: utf-8
'''
Created on 2017-1-13

@author: Administrator
'''

'''
    r:只读
    w:写入

读
content = f.read(n)         读取N bytes的数据
content = f.readline()      读取一行
content = f.readlines()     读取所有行，储存在列表中，每个元素是一行
写
f.write('xxxx')
关闭 f.close()
'''

f = open('D:\\workSpace_python\\record.txt','w')
f.write('tom, 12, 86\n')
f.write('Lee, 15, 99\n')
f.write('Lucy, 11, 58\n')
f.write('Joseph, 19, 56\n')

f.close()

f = open('D:\\workSpace_python\\record.txt','r')
#print len(f.readlines())
#line = f.readline()
#while line:
#    print line
#    line = f.readline()
    
#for line in f:
#    print line

lins = f.readlines()
for line in lins:
    print line