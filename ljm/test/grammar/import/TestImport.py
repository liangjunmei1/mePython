#!/usr/bin/python
# -*- coding: utf-8 -*-

from ljm.test.grammar.exception.MeException import *
# from ljm.test.exception.MeException import MeException

'''
模块：在python中，一个.py文件就构成一个模块
模块的引用方式：
    1. import a as b    引入模块a，重命名为b
    2. from a import function1 从模块a中引入函数function1，调用a中的对象时直接写 function1，而不再是 a.function1
    3. from a import * 从模块中引入所有对象，调用a中对象时，可以直接使用对象，而不再是 a.对象

模块包的引入
    import this_dir.module  引入this_dir 文件夹下面的 module模块
'''
class TestImport():

    def test_import(self):
        """
        import * 的写法
        """
        MeException.IOError()
        MeException().IOError()
        MeException.KeyError(self)
        MeException().KeyError(self)


if __name__=="__main__":
    TestImport().test_import()