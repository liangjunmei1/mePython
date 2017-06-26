#coding:utf-8
'''
 算法: 循环
循环的四要素:
    1：定义循环变量
    2：循环条件
    3：循环体(最重要的部分)
    4：循环变量发生变化
并不是按照1、2、3、4 步骤进行，而是先实现循环体，然后再逐渐完善
将程序做成 循环体的步骤:
    1：确定循环体，将循环体全部选中，用Tab建内推，用while 循环包裹
    2：从上往下分别写 1、2、4
    3：在python 里面有:就没有()
     定义循环变量
  while 循环条件:
            循环体
           循环变量发生变化

i = 0
while i<5:
    a = input("请输入数字:")
    print a
    i+=1

i = 0
while i <=100:
    a = input("请输入成绩:")
    if a >=0 and a <=100:
        if a>90 and a<=100:
            print '您的成绩非常优秀，A'
        elif a>80 and a<=90:
            print '您的成绩很好，B'
        elif a>70 and a<=80:
            print '您的成绩不错，C'
        elif a>=60 and a<=70:
            print '您的成绩不错，D'
        else:
            print '您的成绩不及格，E'
    else:
        print "您输入的成绩不正确"
    i+=1
'''
'''
for 循环
语法:    
    for 变量  in 序列:
                    循环体
                    
range(n)       产生一个 0 到  n-1 的序列
range(m,n)     产生一个  m 到  n-1 的序列 
range(m,n,i)   产生一个  m 到  n-1 的序列 ，并且步长为 i
'''
for i in range(1,101):
    print i,'ok'
