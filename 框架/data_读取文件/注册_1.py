#!/usr/lib/env python
#--*-- conding=utf-8 -*-
import xlrd
class shuju():
    def zhuce(self):
        shuju=[]
        f=xlrd.open_workbook(r'C:\Users\LIU\Desktop\python\框架\data_读取文件\注册.xlsx')
        sheet=f.sheets()[0]
        hang=sheet.nrows
        for i in range(hang):
            nei=sheet.row_values(i)
            shuju.append(nei)
        return shuju
a=shuju()
a.zhuce()