#coding = utf-8
import unittest

#加载测试文件

import ljm.test.self_study_more.selenium2.unit_test.module.testadd
import ljm.test.self_study_more.selenium2.unit_test.module.testsub

#构造测试集

suite = unittest.TestSuite()

suite.addTest(ljm.test.self_study_more.selenium2.unit_test.module.testadd.TestAdd('test_add'))
suite.addTest(ljm.test.self_study_more.selenium2.unit_test.module.testadd.TestAdd('test_add2'))
suite.addTest(ljm.test.self_study_more.selenium2.unit_test.module.testadd.TestAdd('test_add3'))


suite.addTest(ljm.test.self_study_more.selenium2.unit_test.module.testsub.TestSub('test_sub'))
suite.addTest(ljm.test.self_study_more.selenium2.unit_test.module.testsub.TestSub('test_sub2'))



if __name__ == '__main__':

    #执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
