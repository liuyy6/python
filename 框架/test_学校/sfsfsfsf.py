import unittest
from 框架.data_读取文件.a_2 import duqu
from 框架.config_配置_公共性.a_1 import 学校_查询
class haofenshu(unittest.TestCase):
    shuju=duqu().tes_shuju()
    jiekou=学校_查询.学校_快查
    def test_1(self):
        html = self.jiekou(self.shuju[0][0])
        self.assertNotEqual(html['code'], int(self.shuju[0][1]))
    def test_2(self):
        html = self.jiekou(self.shuju[1][0])
        self.assertEqual(html['code'], int(self.shuju[1][1]))
    def test_3(self):
        html = self.jiekou(self.shuju[2][0])
        self.assertNotEqual(type(html['data']),self.shuju[2][2])