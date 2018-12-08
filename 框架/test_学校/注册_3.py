#!/usr/lib/env python
#--*-- coding=utf-8 -*-
import unittest
from 框架.config_配置_公共性.注册_2 import qing
class test_zhuce(unittest.TestCase):
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def test_1(self):
        aa=qing().qi(self.a,self.b)
        self.assertEqual(aa['code'],self.b)


