#coding=utf-8
'''
Created on 2017年1月27日

@author: Administrator
'''
import os

class File():
    
    def readFile(self):
        f = os.path.abspath(r"D:\ljm\workSpacePython\LearnPython\src\com\yumimobi\basegrammar\file.txt")
        try:
            file = open(f,'r')
            list =  file.readlines()
            for readLine in list:
                print readLine
        except Exception,e:
            print e
        finally:
            file.close()
            
    def scoreFile(self):
        f = os.path.abspath(r"D:\ljm\workSpacePython\LearnPython\src\com\yumimobi\basegrammar\file.txt")
        list3 = []
        try:
            file = open(f,'r')
            list =  file.readlines()
            for readLine in list:
                list2 = readLine.split(",")
#                 print list2[2].replace("\n","")
                if (int(list2[2].replace("\n","")) < 60):
                    print "得分小于60的人是：",list2[0]
                if (list2[0][0] == 'L'):
                    print "名字是L开头的人：",list2[0]
                list3.append(int(list2[2].replace("\n","")))
            print "所有人的总分之和： ",sum(list3)
        except Exception,e:
            print e
        finally:
            file.close()
            
    def updateFile(self):
        f = os.path.abspath(r"D:\ljm\workSpacePython\LearnPython\src\com\yumimobi\basegrammar\file.txt")
        list3 = []
        try:
            file = open(f,'a')
            list =  file.readlines()
            for readLine in list:
                list2 = readLine.split(",")
                list3.append(list2[0])
                if(list3[0][0].capitalize()=="True"):
                    print "首字母是大写"
                else:
                    print "首字母是小写",list3[0][0],list3[0][0].title()
        except Exception,e:
            print e
        finally:
            file.close()
            
if __name__=="__main__":
    f = File()
    f.updateFile()