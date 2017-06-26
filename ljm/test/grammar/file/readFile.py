#coding=utf-8
'''
Created on 2016-2-14

@author: ljm
'''
#一般用于处理python 的日志
file = open("MyTesting.txt","r")
readfilecontent = file.read()
readline =  file.readline()    
readlines = file.readlines()
 
print type(readfilecontent)
print type(readline)
print type(readlines)
#readfilecontent = file.read()     #全部读取到内存中
#print readfilecontent
#file.close()

#while True:
#    readline =  file.readline()     #逐行读取，消耗的内存少
#    if not readline: #EOF
#        break
#    else:
#        readline = readline[:-1] #这种逐行读取的时候，readline是一个字符串类，换行的时候会把 \n 拼上字符串一起读出来
#        print readline
#file.close()

#readlines = file.readlines()    #每次读取多行数据，它会在每行的结尾都加上\n
#for line in readlines:
#    print line
#file.close()


#index = 0
#while 1:
#    if index >= len(readlines):
#        break
#    else:
#        print (readlines[index])
#    index = index +1
#file.close()
