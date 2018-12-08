#!/usr/bin/env python
#--*-- coding='utf-8' -*-
from 框架.test_学校.moore_test import yongli
import unittest
import HTMLTestRunnertest
import time
class run():
    def all(self,a):
        suit=unittest.TestSuite()
        for i in a:
            discover=unittest.defaultTestLoader.discover(r'..\test_学校',pattern='{}.py'.format(i))
            suit.addTest(discover)
        now=time.strftime('%Y %m %d %H-%M-%S',time.localtime(time.time()))
        with open('moore.html','wb')as f:
            runner=HTMLTestRunnertest.HTMLTestRunner(tester='刘艳颖',description='测试结果如下',
                                                     title='摩尔招聘测试报告',stream=f)
            runner.run(suit)
            f.close()
a=run()
t=['moore_test']
a.all(t)
