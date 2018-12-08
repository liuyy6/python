#!/usr/lib/env python
# --*-- coding=utf-8 -*-
from 框架.data_读取文件.注册_1 import shuju
from 框架.test_学校.注册_3 import test_zhuce
shu=shuju().zhuce()
for i in range(1,len(shu)):
    a=shu[i][0]
    b=shu[i][1]
    if __name__=='__main__':
        run=test_zhuce()




print(a)