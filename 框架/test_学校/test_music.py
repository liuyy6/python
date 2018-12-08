#!/usr/bin/env python
#--*-- coding:utf-8 -*-
import unittest
from 框架.config_配置_公共性.config_music import aap_1
class wyy_music(unittest.TestCase):
    def test_1(self):
        aa=aap_1().drvice_1()
        self.assertEqual(aa,'我是你的_影')
    def test_2(self):
        aa=aap_1().drvice_2()
        self.assertEqual(aa,'官方榜')