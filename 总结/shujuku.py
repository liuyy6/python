#/usr/lib/env/python
#--*--coding:utf-8 -*-
# import pymysql
#
# abc=pymysql.connect(host='192.168.0.187',
#                     port=3306,
#                     user='root',
#                     password='686789',
#                     charset='utf8')
# abc=pymysql.connect(host='192.168.0.193',
#                 port=3306,user='root',
#                 passwd='123456',charset='utf8')
# aaa=abc.cursor()
# aaa.execute('show databases;')
# aaa.execute('use test2;')
# aaa.execute('show tables;')
# aaa.execute('select * from emp;')      #黄色属于正常
# print(aaa.fetchall())         #读取上一句mysql的结果，所有的结果
# print(aaa.fetchmany(2))       #读取上一句的结果，里面的数字写几就读取几条数据，数字大于
#                               #总数据，则读取全部数据。
# print(aaa.fetchall())         #如果  print(aaa.fetchall(2)) 读取两条，则读取剩余所有数据
# print(aaa.fetchone())         #每次只读取一个结果， 本身具有迭代功能，本身具有累加
# print(aaa.fetchone())
# print(aaa.fetchone())
#################################################################################################
#写入数据库
# aaa=abc.cursor()
# # aaa.execute('create database py112;')
# aaa.execute('use py112')
# #aaa.execute("create table py11(姓名 char(200),年龄 int,性别 char(20));")
# aaa.execute("insert into py11 values('{}',{},'{}');".format('小明',17,'男'))
# abc.commit()
# aaa.execute('select * from py11;')
# print(aaa.fetchall())
##########################################
# aaa=abc.cursor()
# aaa.execute('use py112;')
#aaa.execute('create table biao(名字 char(20),性别 char(10),年龄 int,班级 char(30));')
# for i in range(10):
#     aaa.execute('insert into biao values("{}","{}",{},"{}");'.format('小明','男',i,'一班'))
#     abc.commit()
# aaa.execute('select * from biao;')
# print(aaa.fetchall())
######################################################################################################
#从数据库中读取到文件中

# # #/usr/lib/env python
# # #--*--coding:utf-8 -*-
# aaa=abc.cursor()
# aaa.execute('use py112;')
# aaa.execute('select * from biao;')
# yuanzu=(aaa.fetchall())
# aaa.execute('desc biao;')
# biaotou=(aaa.fetchall())
# with open('a.txt','w',encoding='utf-8') as f:
#     for i in range(len(biaotou)):
#         if i==len(biaotou)-1:
#             f.write('{}'.format(biaotou[i][0],))
#             f.write('\n')
#         else:
#             f.write('{},'.format(biaotou[i][0]))
#     for j in range(len(yuanzu)):
#             f.write('{},{},{},{}'.format(yuanzu[j][0],yuanzu[j][1],yuanzu[j][2],yuanzu[j][3]))
#             f.write('\n')
# print(yuanzu)
# print()
# print(biaotou)
###############################################################################
# import pymysql
# #
# abc=pymysql.connect(host='39.105.101.238',
#                     port=3306,
#                     user='root',
#                     password='Benkint@1029',
#                     charset='utf8')
# aaa=abc.cursor()
# aaa.execute('show databases')
# print(aaa.fetchall())
# aaa.execute('use lv_front;')
# aaa.execute('show tables;')
# b=aaa.fetchall()
# print(b)
# #aa.execute('select * from x$waits_global_by_latency;')
# #print(aaa.fetchall())
##########################################################
#数据库练习
# import pymysql
# abc=pymysql.connect(host='192.168.0.187',
#                     port=3306,
#                     user='root',
#                     password='686789',
#                     charset='utf8')
# aaa=abc.cursor()
# aaa.execute('use py1')
#aaa.execute('show tables')
# aaa.execute('create table jb1(学号 int,姓名 char(20),年龄 int );')
# for i in range(30):
#     aaa.execute('insert into jb1 values({},"{}",{});'.format(20180712,'小李',i))
#     abc.commit()
#########
# a=aaa.execute('select * from jb1;')
# a=aaa.fetchall()
# with open('a.txt', 'w', encoding='utf-8') as f:
#     f.write('"{}","{}","{}"'.format('学号','姓名','年龄'))
#     f.write('\n')
#     for i in range(len(a)):
#         f.write('{},"{}",{}'.format(a[i][0]+i,a[i][1],a[i][2]))
#         f.write('\n')
################################################################################
# aaa=abc.cursor()
# aaa.execute('show databases')
# aaa.execute('use py1')
# aaa.execute('desc jb1')
# q=aaa.fetchall()
# aaa.execute('select * from jb1')
# b=aaa.fetchall()
# with open('b.txt','w',encoding='utf-8') as f:
#     f.write('"{}","{}","{}";'.format(q[0][0],q[1][0],q[2][0]))
#     f.write('\n')
#     for i in b:
#         print(i)
#         f.write('{},"{}",{}'.format(i[0],i[1],i[2]))
#         f.write('\n')
#################################################################3333
# aaa=abc.cursor()
# aaa.execute('use py1')
# aaa.execute('drop tables day2;')
# aaa.execute('create table day2(学号 int,姓名 char(20),年龄 int );')
# with open("a.txt","r",encoding="utf-8") as f:
#     aa = f.readlines()
#     for j in range(1,',')len(aa)):
# # #         a=aa[j].split(
#         aaa.execute("insert into day2 values({},'{}',{});".format(a[0],a[1],a[2]))
# aaa.execute('select * from day2;')
# print(aaa.fetchall())