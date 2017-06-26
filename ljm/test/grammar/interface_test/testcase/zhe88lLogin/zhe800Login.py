#coding:utf8
import cookielib,urllib2
from self_study.web.project5.project_combat.testcase.zhe88lLogin.zhe800_login_headers import zhe800_login_headers

class Login(object):
    def __init__(self):
        self.url = "http://www.zhe800.com/login?return_to=http%3A%2F%2Fwww.zhe800.com%2F%3Futm_content%3DT_title%26jump_source%3D1%26qd_key%3DXucS9iov%26utm_source%3Dbaidupz"
    
    def test_zhe800_login(self):
        cookie = cookielib.CookieJar
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
        opener.addheaders = zhe800_login_headers
        
        response = opener.open(self.url)
        result = response.read()
        print result
        
print Login.test_zhe800_login()