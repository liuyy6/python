#！/usr/bin/env python
#--*-- coding:utf-8
import xlrd
class duqu():
    def tes_shuju(self):
        shuju = []
        f = xlrd.open_workbook(r'..\data_读取文件\test.xls')
        sheet = f.sheets()[0]
        num = sheet.nrows
        for i in range(1, num):
            aa = sheet.row_values(i)
            shuju.append(aa)
        return shuju
    def tes_shuju_2(self):
        f = open(r'C:\Users\LIU\Desktop\python\框架\data_读取文件\a.txt','r')
        f = f.read().replace('\n', ',')
        mu = f.split(',')
        return mu


a=duqu()
a.tes_shuju_2()
