#coding:utf-8
'''运行测试方法'''
from self_study.web.project5.project_combat.run.runAllClass import list_class
import HTMLTestRunner,unittest,time

def test_suite_run():
    path = "D:\\"
    filename = path + time.strftime("%Y-%m-%d-%H-%M-%S-") + "result.html"
    fp = file(filename,"wb")
    suite = unittest.TestSuite()
    for key in list_class:
        suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(key))
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title="51Testing  Result:",description="51Testing  Test Report:")
    runner.run(suite)
    
test_suite_run()