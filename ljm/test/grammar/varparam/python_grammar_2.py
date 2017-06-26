#coding:utf-8
'''
    算法: 分支
    语法:
    if 条件:
                语句体
    else:
               语句体

while True:
    try:
        a = input()
    except NameError:
        print '请输入正确的数字'
        continue
    else:
        break
    
a = input('请输入数值:')
if a>0:
    print a+1
else:
    print a-1
    ''' 
   
'''
    算法: 分支
    语法:
    if 条件1:
                语句体1
    elif 条件2:
               语句体2
    elif 条件3:
               语句体3
    else 
             语句体4
python 里面条件连接就是只有 and 和 or ，没有 && 和 ||
''' 
a = input("请输入您的成绩:")  
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
    

