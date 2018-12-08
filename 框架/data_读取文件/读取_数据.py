#！/usr/bin/env python
#--*-- coding:utf-8
import xlrd
class duqu():
    def tes_shuju(self):
        shuju = []
        f = xlrd.open_workbook(r'C:\Users\LIU\Desktop\python\框架\data_读取文件\test.xls')
        sheet = f.sheets()[0]
        num = sheet.nrows
        # print(num)
        for i in range(1, num):
            aa = sheet.row_values(i)
            shuju.append(aa)
        # print(shuju)
        return shuju