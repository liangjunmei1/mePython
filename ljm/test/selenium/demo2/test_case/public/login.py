#coding=utf-8


def login(self,username,password):
    
    driver = self.driver
    driver.implicitly_wait(5)
    
    driver.find_element_by_xpath('/html/body/div/div/p/a').click()
    driver.find_element_by_name("login_info").clear()               #
    driver.find_element_by_name("login_info").send_keys(username)   #输入用户名
    driver.find_element_by_name("password").clear()                 #
    driver.find_element_by_name("password").send_keys(password)     #输入密码
    driver.find_element_by_class_name("submit_login").click()       #点击登录
    
def logout(self):
    driver = self.driver
    driver.find_element_by_link_text(u"安全退出").click()
