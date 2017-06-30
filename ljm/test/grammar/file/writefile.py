#coding=utf-8
'''
Created on 2016-2-14
@author: ljm
'''

#fh = open("test.txt","w")
#fh.write("str")
#fh.close

#逐行写入文件
#fh = open("test.txt","w")
#strlist = ['a','b','c','d']
#fh.writelines(strlist)
#fh.close

#在文件末尾追加内容 add
fh = open("test.txt","a")
fh.write("str")
fh.close


#判断文件的打开方式
print fh.mode
