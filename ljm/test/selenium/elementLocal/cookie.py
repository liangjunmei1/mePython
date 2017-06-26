#coding=utf-8
'''
Created on 2017年1月27日

@author: Administrator
'''
import os,time
from selenium import webdriver

class Cookies():
    def __init__(self):
        
        # os.path.abspath(path) 返回绝对路径
        print os.path.abspath("../")
        firefoxBin = os.path.abspath(r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe")
        os.environ["webdriver.firefox.bin"] = firefoxBin
        
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.baidu.com")
        self.driver.quit()
        
    def printCookie(self):
        print  self.driver.get_cookies()
        self.driver.quit()
        
    def addCookie(self):
        dist = {'name':'key-aaa','value':'value-bbb'}
        self.driver.add_cookie(dist)
        
        for cookie in self.driver.get_cookies():
            print '%s--->%s' % (cookie['name'],cookie['value'])
       
        self.driver.quit()
        
    def delCookie(self):
        self.driver.delete_cookie("key-aaa")
        self.driver.delete_all_cookies()
        print self.driver.get_cookies()
        
        self.driver.quit()
if __name__=="__main__":
    c = Cookies()
#     c.printCookie()
#     c.addCookie()
#     c.delCookie()