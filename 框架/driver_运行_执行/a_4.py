#！/usr/bin/env python
#--*-- coding:utf-8

from 框架.data_读取文件.a_2 import duqu
from 框架.report_测试报告.a_5 import Test_run
if __name__=='__main__':
    run=Test_run()
    mu=duqu().tes_shuju_2()
    if 'all' in mu:
        run.run_read('*.')
    else:
        run.run_read(mu)
