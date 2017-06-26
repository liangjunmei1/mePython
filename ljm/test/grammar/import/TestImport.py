#!/usr/bin/python
# -*- coding: utf-8 -*-

from ljm.test.grammar.exception.MeException import *
# from ljm.test.exception.MeException import MeException

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