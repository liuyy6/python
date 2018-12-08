#！/usr/bin/env python
#--*-- coding:utf-8
import unittest
import HTMLTestRunnertest
import time
class Test_run():
    def run_read(self, a):
        suit = unittest.TestSuite()
        for i in a:
            discover = unittest.defaultTestLoader.discover(r'..\test_学校', pattern='{}.py'.format(i))
            suit.addTest(discover)  # 文件夹名         正则匹配文件
        now = time.strftime('%Y %m %d %H-%M-%S', time.localtime(time.time()))
        f = open('abc.html', 'wb')
        runner = HTMLTestRunnertest.HTMLTestRunner(tester='刘艳颖',
                                                   description='测试结果如下：',
                                                   title='好分数测试报告',
                                                   stream=f)
        runner.run(suit)
        f.close()
