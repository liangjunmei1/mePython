#coding = utf-8
#from 后面的路径只到文件名 import 后面是类名
from count import Count
#测试两个数相加

class TestCount:

    def test_add(self):
        try:
            j = Count(2,4)
            add = j.add()
            assert(add == 6),'Integer addition result error!'
        except AssertionError,msg:
            print msg
        else:
            print 'test pass!'

#执行测试类
mytest=TestCount()
mytest.test_add()
