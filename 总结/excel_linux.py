# import xlwt    #只能写入，写入excel表格数据
import xlrd
import xlutils
# #打开一个空白文件,括号内可以写，也可以不写
# # （编码方式，默认的是这个文件前两行已经注释了 coding：utf-8）
# f=xlwt.Workbook()
# #添加一个标签页，括号中写标签页中的名称
# sheet=f.add_sheet('python操作excel')
# #写入数据
# # 第一个代表多少行   第二个代表多少列   第三个代表写入的内容
# sheet.write(0,0,'内容')  #写在了第一个格子里
# #保存文件
# f.save('text.xls')
#
# #################################################################
#脚本练习
# import xlwt
# f=xlwt.Workbook()
# sheet1=f.add_sheet('python脚本练习')
# sheet1.write(0,0,'姓名')
# sheet1.write(0,1,'年龄')
# sheet1.write(0,2,'班级')
# for i in range(1,31):
#     sheet1.write(i,0,'小明')
#     sheet1.write(i,1,'18')
#     sheet1.write(i,2,'一班')
# f.save('批量导入1.xls')
##########################################################################
#脚本练习2     数据库的批量导入
import pymysql
# import xlwt
abc=pymysql.connect(host='192.168.0.187',
                    port=3306,
                    user='root',
                    password='686789',
                    charset='utf8')
# aaa=abc.cursor()
# # aaa.execute('use py1')
# # aaa.execute('select * from jb1')
# # a=aaa.fetchall()
# aaa.execute('desc jb1')
# b=aaa.fetchall()
# x=xlwt.Workbook()
# sheet=x.add_sheet('shujuku')
# for i in range(len(b)):
#     sheet.write(0,i,b[i][0])
# for j in range(1,len(a)):
#     for jj in range(3):
#         sheet.write(j,jj,a[j-1][jj])
# x.save('shuju.xls')

# aaa=abc.cursor()
# aaa.execute('show databases')
# print(aaa.fetchall())
######################################################################################################
#excel的读取
import xlrd
#打开一个文件（文件名）
#f=xlrd.open_workbook('shuju.xls')
################    两种获取标签页方式   1，通过索引
# sheet=f.nsheets                           #获取总共有多少个标签页
# print(sheet)
# sheet=f.sheets()[0]                          #索引获取标签页

# print(sheet.nrows)                           #获取有多少行
# for i in range(sheet.nrows):
#     print(sheet.row_values(i))                 #row_values(),读取第几行的内容，第一行从0读取

# print(sheet.ncols)                              #获取有多少列
# print(sheet.col_values(0))                  #读取第几列内容，第一列从0开始
# print(sheet.cell(0,0).value)                     #读取某个单元格内容
###############第二种方式获取标签页
# import xlrd
# #打开一个文件（文件名）
# f=xlrd.open_workbook('批量导入2.xls')       #打开这个文件
# print(f.sheet_names())                         #获取所有标签页名称
# sheet=f.sheet_by_name('python脚本练习')            #括号内填写操作的标签页名称
#
# for i in range(sheet.nrows):
#      print(sheet.row_values(i))
#####################################################################################################
#                                                                  从表中导入数据库
import pymysql
import xlrd
import xlwt
# abc=pymysql.connect(host='192.168.0.187',
#                     port=3306,
#                     user='root',
#                     password='686789',
#                     charset='utf8')
# aaa=abc.cursor()
# aaa.execute('show databases;')
# aaa.execute('use py1 ')
# f=xlrd.open_workbook('shuju.xls')
# sheet=f.nsheets
# print(sheet)
# sheet1=f.sheets()[0]
# bb=sheet1.nrows
# print(bb)
# aa=sheet1.row_values(0)
# for i in range(1,bb):
#     cc = sheet1.row_values(i)
#     # print(cc)
#    # aaa.execute('create table day2({} int,{} char(20),{} int;)'.format(aa[0],aa[1],aa[2]))
#     aaa.execute('insert into day2 values({},"{}",{});'.format(cc[0],cc[1],cc[2]))
# aaa.execute('select * from day2;')
# print(aaa.fetchall())
#######################################################################################################
#                                                                从表中导入数据库
# import pymysql
# import xlwt
# abc=pymysql.connect(host='192.168.0.187',
#                     port=3306,
#                     user='root',
#                     password='686789',
#                     charset='utf8')
# aaa=abc.cursor()
# aaa.execute('use py1;')
# aaa.execute('desc day2')
# biaotou=aaa.fetchall()
# aaa.execute('select * from day2;')
# shuju=aaa.fetchall()
# f=xlwt.Workbook()
# sheet=f.add_sheet('数据库到excel')
# for j in range(len(biaotou)):
#     for i in range(len(shuju)):
#         sheet.write(i,j,shuju[i][j])
# f.save('数据库到表.xls')


######################################################################################################
          # excel  追加
# import xlrd
# from xlutils.copy import copy     #某一个文件夹下面读取函数
# f=xlrd.open_workbook('shuju.xls')
# #复制文件
# new_f=copy(f)
# #操作的是复制的文件
# sheet=new_f.get_sheet(0)    #通过索引复制标签页      只能通过索引获取标签页
# sheet.write(5,6,'sfdfsdfsfs')
# new_f.save('shuju.xls')
################################################################################################
#  接
####################################################################################3
#创建一个传输通道             文件互传
# import paramiko
# ssh123=paramiko.Transport(('192.168.0.187',22))    #这个函数只能接受元组，所以双括号
# ssh123.connect(username='root',password='686789')
# #传输文件     使用的是 sftp 协议， 创建一个sftp的实例
# sftp=paramiko.SFTPClient.from_transport(ssh123)
# #get是从linux下载文件到本地
# sftp.get('/home/liu/7410','.7410')         #   .7410 代表当前路径
# #put是从本地向linux上，上传文件
# sftp.put('shuju.xls','/home/liu/shuju.xls')

# import os
# os.rename('excel表格.py','excel_linux.py')




