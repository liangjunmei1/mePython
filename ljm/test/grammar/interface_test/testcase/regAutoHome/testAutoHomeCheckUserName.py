#coding:utf8
'''接口测试post请求'''
from self_study.web.project5.project_combat.data.testData import autoHomeRegCheckUserName
import urllib,unittest,json

class CheckUserName(unittest.TestCase):
    
    def setUp(self):
        pass
    def testRegCheckUserName(self):
        httpReq = urllib.urlopen(autoHomeRegCheckUserName[0],urllib.urlencode(autoHomeRegCheckUserName[1]))
        httpResultJson = json.loads(httpReq.read())
        print httpResultJson
        
        self.assertEqual(httpResultJson['Message'],'Msg.UserNameSuccess')
        self.assertEqual(httpResultJson['BanWord'], None)
        self.assertEqual(httpResultJson['RecommendNameList'], None)
        self.assertEqual(httpResultJson['Success'], 1)
        
if __name__ == "__main__":
    unittest.main()