#coding:utf-8
'''
自动化执行用例—selenium
1.调用webdriver函数启动浏览器，使用get方法访问目标网址
2.通过页面元素属性定位登录对象，使用click方法点击登录
3.通过页面元素属性定位用户名对象，使用send_keys方法输入用户名
4.通过页面元素属性定位密码对象，使用send_keys方法输入密码
5.通过页面元素属性定位登录按钮，使用click方法点击登录
6.通过断言函数，比对实际结果和预期结果
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()                    #调用 webdriver 打开火狐
driver.maximize_window()                        #最大化浏览器
driver.get('http://172.31.4.124:8888/iwebshop/') #访问目标网址

driver.find_element_by_link_text('登录').click() #定位元素，并执行方法
driver.find_element_by_name("login_info").send_keys('ljm')
driver.find_element_by_name("password").send_keys('123456789')
driver.find_element_by_class_name("submit_login").click()

driver.implicitly_wait(5)                       #等待时间不固定，最大等待5秒
#time.sleep(5)                                   #强制等待，等待时间固定，无论渲染元素是否成功，都等待5秒

#登录成功之后，输入ipad 进行搜索
driver.find_element_by_xpath("/html/body/div/div[3]/div[2]/form/input").send_keys('book')
#定位到要悬停的元素
above = driver.find_element_by_xpath("/html/body/div/div[3]/div[2]/form/input[2]")
#对定位到的元素执行悬停操作
ActionChains(driver).move_to_element(above).perform()
driver.find_element_by_css_selector("html body.index div.container div.searchbar div.searchbox form input.btn").click()

#driver.quit()                                   #退出浏览器，关闭资源
#driver.close()                                  #只是单纯的关闭页面
#driver.back()                                   #后退
#driver.forward()                                #前进，回到上一步
#driver.refresh()                                #刷新