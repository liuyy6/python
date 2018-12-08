#!/usr/bin/env python
#--*-- coding='utf-8' -*-
import unittest
from 框架.config_配置_公共性.moore_config import moore
from 框架.driver_运行_执行.moore_driver import zidonghua
class yongli(unittest.TestCase):
    def test_1(self):
        a=zidonghua().web_1()
        self.assertEqual(a,2)
    def test_2(self):
        a=zidonghua().web_2()
        self.assertEqual(a, 2)

if __name__=='__main__':
    unittest.main()
