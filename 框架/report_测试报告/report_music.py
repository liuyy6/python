#!/usr/bin/env python
#--*-- coding:utf-8 -*-
import unittest
import time
import HTMLTestRunnertest
def music(a):
    suit = unittest.TestSuite()
    for i in a:     # 将整个类中的所有测试用例，添加到测试套件中
        discover=unittest.defaultTestLoader.discover(r'..\test_学校', pattern='{}.py'.format(i))
        suit.addTest(discover)
    now = time.strftime('%Y %m %d %H-%M-%S', time.localtime(time.time()))
    with open(r'app.html', 'wb')as f:
        runner = HTMLTestRunnertest.HTMLTestRunner(tester='刘艳颖',
                                                    description='测试结果如下：',
                                                    title='网易云音乐',
                                                    stream=f)
        runner.run(suit)