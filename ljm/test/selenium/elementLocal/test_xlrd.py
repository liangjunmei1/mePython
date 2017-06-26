#coding:utf-8
'''
      需要将excel 存为文本格式
      自动循环登录
'''
import xlrd
from selenium import webdriver

wb = xlrd.open_workbook("D:\Book.xls")  #打开一个excel
sh = wb.sheet_by_index(0)  #打开第一个工作簿
#获取行数
rows = sh.nrows
A1 = sh.cell_value(1, 0)   #得到第二行第一列的值
A2 = sh.cell_value(1, 1)   #得到第二行第二列的值

print A1, A2

driver = webdriver.Firefox()                    #调用 webdriver 打开火狐
driver.maximize_window()                        #最大化浏览器
driver.get('https://www.baidu.com/') #访问目标网址
    
i = 1
for i in range(1, rows):                #循环excel表格的行数
    print i

    driver.find_element_by_link_text("登录").click() 
    driver.find_element_by_id("TANGRAM__PSP_8__userName").send_keys(sh.cell(i, 0).value)
    driver.find_element_by_id("TANGRAM__PSP_8__password").send_keys(sh.cell(i, 1).value)
    driver.find_element_by_id("TANGRAM__PSP_8__submit").click()
            
    driver.quit()
        
    print sh.cell(i, 0).value, '登陆成功!'
