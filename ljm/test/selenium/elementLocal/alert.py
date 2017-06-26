#coding=utf-8
'''
Created on 2017年1月27日

@author: Administrator
'''
import os,time
from selenium import webdriver

firefoxBin = os.path.abspath(r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe")
os.environ["webdriver.firefox.bin"] = firefoxBin

driver = webdriver.Firefox()

alert = driver.switch_to_alert()
alert.accept()  #确定
alert.dismiss() #取消

alert.text()    #打印文本信息
alert.send_keys("")
