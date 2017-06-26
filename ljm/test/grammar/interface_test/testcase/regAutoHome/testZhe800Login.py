#coding:utf8
'''接口测试get请求'''
from self_study.web.project5.project_combat.data.testData import zhe800Login
import urllib,unittest

class Login(unittest.TestCase):
    
    def testLogin(self):
        
        httpReq = urllib.urlopen(zhe800Login[0]+"?"+urllib.urlencode(zhe800Login[1]))
        print httpReq.read()
        
if __name__ == "__main__":
    unittest.main()