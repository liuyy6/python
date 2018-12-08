#！/usr/bin/env python
#--*-- coding:utf-8
import unittest
import HTMLTestRunnertest
from 框架.test_学校.test_实验 import 学校
import time
class Test_run():
    def run_多个(self):
        suit = unittest.TestSuite()
        suit.addTest(unittest.makeSuite(学校))
        now = time.strftime('%Y %m %d %H-%M-%S', time.localtime(time.time()))
        with open('abc.html', 'wb')as f:
            runner = HTMLTestRunnertest.HTMLTestRunner(tester='刘艳颖',
                                                       description='测试结果如下：',
                                                       title='好分数测试报告',
                                                       stream=f)
            runner.run(suit)
            f.close()
    def run_all(self):
        suit=unittest.TestSuite()
        discover=unittest.defaultTestLoader.discover(r'..\test_学校',pattern='*.py')
        suit.addTest(discover)                           #文件夹名         正则匹配文件
        now = time.strftime('%Y %m %d %H-%M-%S', time.localtime(time.time()))
        f=  open('abc.html', 'wb')
        runner = HTMLTestRunnertest.HTMLTestRunner(tester='刘艳颖',
                                                       description='测试结果如下：',
                                                       title='好分数测试报告',
                                                       stream=f)
        runner.run(suit)
        f.close()
if __name__=='__main__':
    run=Test_run()
    # run.run_多个()
    run.run_all()

