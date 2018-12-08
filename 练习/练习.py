# d=['ws','asda','31']
# a=['qewrq','wqr',['qr','dg'],1312,432,d]
# a.insert(1,111111111)
# a[6].append('qqqqqqqqqqqqq')
# print(a)
# a.sort()
# a.reverse()
# print(a)

# a='jdfsfhkjsdh'
# b=list(a)
# print(b)
# c=str(b)
# print(c)
# a=[2341,'ewrqer']
# b=['sda','sadfa',6523567]
# a.extend(b)
# print(a)
# a=[2313,12321,213,43,43,123]
# b=set(a)
# print(b)
# c=list(b)
# print(c)
# c.sort()
# print(c)
# c.reverse()
# print(c)
# a=24+23423+2423+23432423
# b=a*2
# print(a)
# print(b)
# print('3+4')
# a=[12,32,1,'23',132]
# print('23' in a)
# print(3 + 1)
# print(9 > 23)
# a=4+5
# b=4+6
# a +=b
# print(a)
# a=138487578747
# b=8787643
# if a>b:
#     print('a>b')
# elif a==b:
#     print('a=b')
# else:
#     print('a not= b')
# a=input('请输入：')
# b=int(a)
# if 100>=b>=90:
#     print('优秀')
# elif 90>b>=80:
#     print('良好')
# elif 80>b>=70:
#     print('及格')
# else:
# #     print('废柴')
# a=input('请输入')
# if a.startswith('a') and a.endswith('c'):
#     print('helle world')
# elif a.startswith('a'):
#     print('helle')
# elif a.endswith('c'):
#     print('world')
# else:
#     print(123)
# if (not a.startswith('a')) and (not a.endswith('c')):
#     print('123')
# else:
#     if a.startswith('a')and not a.endswith('c'):
#         print('helle')
#     else:
#         if a.endswith('c') and (not a.startswith('a')):
#             print('world')
#         else:
#             print('helle world')


# if a.startswith('a'):
#     if a.endswith('c')
#         print('helle world')
#     else:
#         print('world')
# elif a.endswith('c')
#     print('hello')
# else:
#     print('123')


# c=input('请输入：')
# b=c.split(',')
# a=[6,6,6]
# a.sort()
# if a[1]+a[0]>a[2]:
#     if a[1]**2+a[0]**2==a[2]**2:
#         print('直角三角形')
#     elif a[1]**2+a[0]**2>a[2]**2:
#         print('锐角三角形')
#     else:
#         print('钝角三角形')
# else:
#     print('不是三角形')

# d=input('请输入：')
# e=d.split(',')
# e.sort()
# a=int(e[0])
# b=int(e[1])
# c=int(e[2])
# if a+b>c:
#     if a**2+b**2==c**2:
#         print('直角')
#     elif a**2+b**2<c**2:
#         print('钝角')
#     else:
#         print('锐角')
# else:
#     print('不是三角形')

# a='qwewq'
# print(a.startswith('w'))

# b=['dfsdfs','sdf','234',34234]
# b.insert(1,'qqqqqqqqq')
# b.append(1111111)
# print(b)
# a=len(b)
# print(a)
# a=12312
# print(a)
# a='121312124'
# print(a[::-1])
# import copy
# b=['123',['1212',[121],1123,'1231']]
# a=['afsaf','fsaf',2342,b87]
# a[3][1][1].append('111111111111111111111111111')
# c=copy.deepcopy(a)
# print(c)
# a=[123,31,13,31312,313,12,13]
# b=['qeq','qeq','dss','fdsd']
# a.extend(b)
# print(a)
# a=(12,343,34,2,342,34,23)
# b=a.count(34)
# print(b) '/n'
# print(a)
# import sys; x = 'runoob'; sys.stdout.write(x + '\n')
#a={'age':213,'name':23}
# b={'age':'sds','we':(13,213,13)}
# a['intt']=1111111
# a.update(b)
# e=a.values()
# print(e)
# a={'name':'小明','age':18,'sex':'男'}
# a.pop('sex')
# a['sex']='nan'
# b=a.keys()
# c=a.values()
# d=a.items()
# print(b,c,d)

#
# a=0
# for i in range(1,101):
#     a+=i
# print(a)
# print(sum(range(101)))
# a={'name':'seds','age':18}
# for i,j in a.items():
#     print(i,j)
# b=0
# a=0
# for i in range(1,100,2):
#     a+=i
# for j in range(0,99,2):
#     b+=j
# print(a-b)
# for i,j range(1,100,2),(0,-99,-2)
# print(sum(range(1,100,2)))
# print(sum(range(0,-99,-2)))
# a=['aas','adad',['das',13],'weqe']
# for i,j in enumerate(a[2]):
#     print(i,j)
# a='dfissddjdskjds'
# for i in enumerate(a):
#     print(i)
# a=['电脑','计算机','mp3']
# for i,j in enumerate(a):
#     print(i+1,j)
# # b=input('请输入：')
# # c=int(b)
# c=int(input('请输入：'))
# print(a[c-1])
# for i in range(1,11,1):
#     if i>5:
#         print(i)
# b=0
# for i in range(1,100):
#     if i%2>0:
#         b+=i
#     else:
#         b-=i
# print(b)




                                                #函数
# def sum1(x=5):      #默认函数             #函数的格式
#     jc=1
#     for i in range(1,x):
#         jc*=i
#     print(jc)
#
# sum1()     #传入新的参数可以替换默认参数       #函数调用

# def hs1(*args):                       可变长参数
#     print(args)                        接收到的是元组
#                                       args:默认规则,变量名
# hs1('qweq',131,'ada',[123,'dsd'])
#
#
# '优先级:
# '必须参数 > 默认参数 > 可变长参数

#                                     四个数字，组合成三位数，不重复
# a=input('>>>>>>>')
# a=a.split(',')
# b=[]
# qc=set()
# for i in a:
#     intt=int(i)
#     b.append(intt)     #字符串转化为数字
# for b1 in range(4):
#     b11=b[b1]           #提取将要删除的元素
#     b.pop(b1)
#     for q in range(len(b)):
#         for j in range(len(b)-1):
#             b[j],b[j+1]=b[j+1],b[j]    #排列组合
#             w=tuple(b)                  #转化成元组
#             qc.add(w)                  #加入到集合，去重
#     b.insert(b1,b11)                 #上面删掉一个元素，补充进元素
# for qcf in qc:                      #在集合中提取元素，组合成的数字（元组形式）
#     for z in qcf:
#         zf=int(z)
#         print(zf,end='')          #将元组中中数据提取出来，元组转化成数字
#     print()
###################################################################
# aa=lambda x,y:x+y+y+x
# print((aa(2,7)))
# 计算器                                      #计算器
# aa=lambda x,y:x+y
# bb=lambda x,y:x-y
# cc=lambda x,y:x*y
# dd=lambda x,y:x/y
# a=input('>>>>>>>')
# a=a.split(',')
# x=int(a[0])
# d=a[1]
# y=int(a[2])
# if d== '+':
#     print(aa(x,y))
# elif d=='-':
#     print(bb(x,y))
# elif d=='*':
#     print(cc(x,y))
# elif d=='/':
#     print(dd(x,y))

########################################################
# a=input('>>>')                        因数之和
# n=int(a)
# for b in range(1,n):
#     yin = 0
#     for i in range(1,b):
#         yu=b%i
#         if yu==0:
#             yin+=i
#     if yin==b:
#         print(b)
#
##############################################################################################
#九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{}*{}={}'.format(i,j,i*j),end='\t')
#     print()
#####################################################
#质数之和
# a=0
# for i in range(2,100):
#     for j in range(2,i+1):
#         if i%j==0:
#             if i!=j:
#                 break
#             else:
#                 a+=i
# print(a)
########################################
#判断三角形：
# a=input('>>>>>>>>')
# a=a.split(',')
# a.sort()
# a1=[]
# for i in a:
#     a=int(i)
#     a1.append(a)
# if a1[0]+a1[1]>a1[2]:
#     if a1[0]**2+a1[1]**2==a1[2]**2:
#         print('直角')
#     if a1[0]**2+a1[1]**2>a1[2]**2:
#         print('锐角')
#     if a1[0]**2+a1[1]**2<a1[2]**2:
#         print('钝角')
# else:
#     print('不是三角形')
###########################################################
# 列表去重排序
# a=input('>>>>>>>>')
# a=a.split(',')
# b=[]
# for i in a:
#     if i not in b:
#         b.append(i)
# b.sort()
# print(b)
#字符串去重排序
# a=input(">>>>>>>>>>>>>>")
# b=set()
# c=[]
# for i in range(len(a)):
#     b.add(a[i])
# for j in b:
#     c.append(j)
# c.sort()
# for b in c:
#     print(b,end='\t')

##################################################################3
#判断回文
# a=input('>>>>>>>>>>>')
# b=0
# for i in range(len(a)):
#     b-=1
#     if a[i]!=a[b]:
#         print('不是回文')
#         break
# else:
#     print(a,'是回文')
#方法二：
# a=input('>>>>>>>')
# b=a[::-1]
# if a==b:
#     print('是回文')
# else:
#     print('不是回文')
########################################################################3
#最大值，最小值
# a=input('>>>>>>>>>>')
# a=a.split(',')
# b=[]
# for i in  a:
#     a=int(i)
#     b.append(a)
# print(max(b),min(b))
###############################################
#打印第一大，第二大
# aa=input('>>>>>>>')
# aa=aa.split(',')
# a=[]
# for i in aa:
#     a.append(int(i))
# a.sort()
# print(a)
# b=a.count(a[-1])
# c=a.count(a[-b-1])
# print(a[-1],b,a[-b-1],c)
# print(aa)
##############################################################################
#排序     冒泡
# a=input('>>>>>>>>>')
# a=a.split(',')
# b=[]
# for i in a:
#     b.append(int(i))
# for jj in range(len(b)-1):
#     for j in range(len(b)-1):
#         if b[j]>b[j+1]:
#             b[j],b[j+1]=b[j+1],b[j]
# print(b)
#选择排序：
# a=input('>>>>>>')
# # a=a.split(',')
# # b=[]
# # for i in a:
# #    b.append(int(i))
# # for j in range(len(b)):
# #     for jj in range(len(b)):
# #         if b[j] > b[jj]:
# #             b[j],b[jj]=b[jj],b[j]
# # print(b)
##############################################################
#杨辉三角你
# a=input('>>>>>>>>>>>>')
# a=int(a)
# b=[]
# for i in range(a):
#     b.append(i)
# b=b[::-1]
# print(b)
# for j in b:
#     for jj in range(j):
#         print('*',end='\t')
#     print()

# a=input('>>>>>>>>')
# a=int(a)
# for i in range(a):
#     print(' '*i,end='')
#     print(' * '*(a-i))

###############################################################################################3
# import os
# # os.rename('py1.py','练习.py')
# # import pymysql
# # abc=pymysql.connect(host='192.168.0.187',
# #                 port=3306,
# #                 user='root',
# #                 password='686789',
# #                 charset='utf8')
# # aaa=abc.cursor()
# # aaa.execute('show databases;')
# # aaa.execute('use py1;')
# # aaa.execute('show tables;')
# # aaa.execute('select * from jb1;')
# # # aaa.execute('select * from jb1 where 年龄>16;')
# # # aaa.execute('select 姓名 from jb1 where 年龄 in (18,19)')
# # # aaa.execute('select * from jb1 order by 年龄 desc;')
# # aaa.execute('select 年龄 from jb1 limit 2,3;')
# # #aaa.execute('desc jb1;')
# # print(aaa.fetchall())
#############################################################################################im
# import pymysql
# import xlrd
# import xlwt
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

# aaa.execute('show tables;')
# aaa.execute('desc article')
# #aaa.execute('select * from article')
# print(aaa.fetchall())

####################################################################################################################
#从表中导入数据库
import pymysql
# import xlwt
# # abc=pymysql.connect(host='192.168.0.187',
# #                     port=3306,
# #                     user='root',
# #                     password='686789',
# #                     charset='utf8')
# # aaa=abc.cursor()
# # aaa.execute('use py1;')
# # aaa.execute('desc day2')
# # biaotou=aaa.fetchall()
# # # print(biaotou)
# # aaa.execute('select * from day2;')
# # shuju=aaa.fetchall()
# # print(shuju)
# # f=xlwt.Workbook()
# # sheet=f.add_sheet('数据库到excel')
# # for j in range(len(biaotou)):
# #     sheet.write(0,j,biaotou[j][0])
# #     for i in range(len(shuju)):
# #         sheet.write(i+1,j,shuju[i][j])
# # f.save('数据库到表.xls')
# # #######################################################################
# # import smtplib
# # import email.mime.text
# # import  email.mime.multipart
# # import os
# # os.rename('邮件.py','邮件,时间.py')
# #######################################################################
# import xlrd
# import xlwt
# # # from xlutils.copy import copy
# # f=xlrd.open_workbook('shuju.xls')
# # #print(f.sheet_names())
# # sheet=f.sheet_by_name('名单')
# # hang=sheet.nrows
# # with open('a.txt','w',encoding='utf-8') as f:
# #     for i in range(hang):
# #         neirong=sheet.row_values(i)
# #         f.write('{}  {}  {}'.format(neirong[0],neirong[1],neirong[2]))
# #         f.write('\n')
# #######################################################
# #表格导入到excel
# # import xlwt
# # e=xlwt.Workbook('utf-8')
# # sheet=e.add_sheet('txt导入表格')
# # for i in range(3):
# #     for j in range(30):
# #         with open('a.txt', 'r', encoding='utf-8') as f:
# #             sheet.write(j,i,'{}'.format(f.readlines()[j].split('  ')[i]))
# # e.save('txt,xls.xls')
# ###########################################################################
# #excel的追加
# # import xlwt
# # # import xlrd
# # # from xlutils.copy import copy
# # # f=xlrd.open_workbook('shuju.xls')
# # # xin=copy(f)
# # # sheet1=f.nsheets
# # # print(sheet1)
# # # print(f.sheet_names())
# # # sheet=xin.get_sheet(0)
# # # print(sheet)
# # # sheet.write(11,11,'幸运')
# # # xin.save('shuju.xls')
# ##########################################
# # import paramiko
# # ssh1=paramiko.SSHClient()
# # ssh1.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# # ssh1.connect(hostname='192.168.5.105',
# #             port=22,
# #             username='root',
# #             password='686789')
# # ssh1.exec_command('ls -al')
# # a,b,c=ssh1.exec_command('ls -al')
# # print(b.read().decode())
# # ssh1.close()
# #####################33
# # a=[12,312,2143,21312,12312]
# # # a.reverse()
# # b=a[::-1]
# # print(a)
# # print(b)
# ####################################
# # import time
# # print(time.time())
# # print(time.strftime('%Y %m %d %H:%M:%S  %A',time.localtime(time.time())))
# # print(time.localtime(time.time()-86400))
# # # print(time.mktime(time.localtime(time.time()-86400)))
# # print(time.strftime('%Y %m %d %H:%M:%S  %w',time.localtime(time.time()-86400)))
# ##############################################################################
# #      https://www.qiushibaike.com/text/page/2/
# # import requests
# # import re
# # class Lx(object):
# #     def qingqiu(self,page):
# #         url='https://www.qiushibaike.com/text/page/{}/'.format(page)
# #         response=requests.get(url=url)
# #         html=response.content.decode('utf-8')
# #         return html
# #     def shaixuan(self,html):
# #         shuju=[]
# #         patt=re.compile('<div class="content">(.*?)</span>',re.S)
# #         ii=patt.findall(html)
# #         for i in ii:
# #             i=i.replace('<span>','').replace('<br/>','\n')
# #             i=i.strip()
# #             shuju.append(i+'\n')
# #         return shuju
# #     def baocun(self,neirong):
# #         with open('aaa.txt','a',encoding='utf-8') as f:
# #             for i in neirong:
# #                 f.write(i+'\n')
# #
# #
# #
# #
# #
# # lx=Lx()
# # html=lx.qingqiu(1)
# # neirong=lx.shaixuan(html)
# # lx.baocun(neirong)
#
# ###################################################################################
# # 'https://www.biqugexsw.com/72_72410/15448963{}.html'.format(+3)
# # # import requests
# # # import re
# # # class Xiaoshuo(object):
# # #     def qingqiu(self,page):
# # #         url='http://www.biqule.com/book_59737/{}.html'.format(17194102+page)
# # #         response=requests.get(url=url)
# # #         html=response.content.decode('gbk')
# # #         #print(html)
# # #         return html
# # #     def guolv(self,htl):
# # #         shuju=[]
# # #         patt=re.compile('<div id="content" name="content">(.*?)</div>',re.S)
# # #         items=patt.findall(htl)
# # #         for i in items:
# # #             i=i.replace('&nbsp;&nbsp;&nbsp;&nbsp;','').replace('\n','').replace('<br />','')
# # #             i=i.lstrip()
# # #             i=i.rstrip()
# # #             i=i.strip()
# # #             shuju.append(i)
# # #         return shuju
# # #     def save(self,sj):
# # #         with open('bb.txt','a',encoding='utf-8') as f:
# # #             for i in sj:
# # #                 i=i.replace('\n','')
# # #                 f.write(i)
# # #
# # # x=Xiaoshuo()
# # # for i in range(283,2224):
# # #     c=x.qingqiu(i)
# # #     sj=x.guolv(c)
# # #     x.save(sj)
# #
# # ###########################################################3
# #   https://book.douban.com/top250?start=0
#
# # import requests
# # import re
# # import xlwt
# # class Shuming(object):
# #     def qingqiu(self,page):
# #         url='https://book.douban.com/top250?start={}'.format(page)
# #         response=requests.get(url=url)
# #         html=response.content.decode('utf-8')
# #         return html
# #     def guolv(self,html):
# #         mu=[]
# #         patt=re.compile('title="(.*?)"',re.S)
# #         itmes=patt.findall(html)
# #         for i in itmes:
# #             if i!='可试读':
# #                mu.append(i)
# #         print(mu)
# #         return mu
# #     def guolvj(self,htm):
# #         patt2 =re.compile('<span class="inq">(.*?)</span>', re.S)
# #         itmes2 = patt2.findall(htm)
# #         print(itmes2)
# #         return itmes2
# #     def save(self,mu,jian):
# #         f=xlwt.Workbook()
# #         sheet=f.add_sheet('shuming')
# #         sheet.write(0,0,'书名')
# #         sheet.write(0,1,'简介')
# #         for i in range(len(mu)):
# #             sheet.write(i+1,0,mu[i])
# #         for j in range(len(jian)):
# #             sheet.write(j+1,1,jian[j])
# #         f.save('shudan.xls')
# #
# #
# #
# #
# #
# # s=Shuming()
# # a=s.qingqiu(0)
# # mu=s.guolv(a)
# # jian=s.guolvj(a)
# # s.save(mu,jian)
# # #################################################################################
# # import requests
# # import re
# # #  爬虫，中国地理
# # class Dli(object):
# #     def qingqiu(self):
# #         url='https://www.sohu.com/a/213443983_744774'
# #         head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
# #         response=requests.get(url=url,headers=head)
# #         html=response.content.decode('utf-8')
# #         # print(html)
# #         return html
# #     def guolv(self,html):
# #         tu=[]
# #         patt=re.compile('src="http://5b0988e595225.cdn.sohucs.com/images/20171229(.*?)" /></p>')
# #         itmes=patt.findall(html)
# #         for i in itmes:
# #             i='http://5b0988e595225.cdn.sohucs.com/images/20171229'+i
# #             tu.append(i)
# #         return tu
# #     def cave(self,tu):
# #         for i,j in enumerate(tu):
# #             head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
# #             response = requests.get(url=j, headers=head)
# #             html = response.content
# #             with open(r'C:\Users\LIU\Desktop\地理中国\{}.jpeg'.format(i),'wb') as f:
# #                 f.write(html)
#
#
#
# # d=Dli()
# # html=d.qingqiu()
# # guo=d.guolv(html)
# # d.cave(guo)
# #######￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥
# #/user/lib/env   python
# #--*-- enconding=utf-8 -*-
# # import pymysql
# # abc=pymysql.connect(host='192.168.0.187',
# #                     port=3306,
# #                     user='root',
# #                     password='686789',
# #                     charset='utf8')
# # aaa=abc.cursor()
# # aaa.execute('show databases;')
# # aaa.execute('use py1')
# # aaa.execute('show tables;')
# # aaa.execute('select *  from jb1;')
# # w=aaa.fetchall()
# # with open('q.txt','w',encoding='utf-8') as f:
# #     for i in w:
# #         print(i)
# #         f.write('{} {} {}'.format(i[0],i[1],i[2]))
# #         f.write('\n')
# #/usr/lib/env python
# #--*-- conding  utf-8 -*-                                库到表
# # import pymysql
# # import xlwt
# # abc=pymysql.connect(host='192.168.0.187',
# #                     port=3306,
# #                     user='root',
# #                     password='686789',
# #                     charset='utf8')
# # aaa=abc.cursor()
# # aaa.execute('show databases;')
# # aaa.execute('use py1')
# # aaa.execute('show tables')
# # aaa.execute('desc jb1')
# # de=aaa.fetchall()
# # aaa.execute('select * from jb1')
# # jb=aaa.fetchall()
# # f=xlwt.Workbook('utf-8')
# # sheet=f.add_sheet('ku')
# # for i in range(len(de)):
# #     sheet.write(0,i,"{}".format(de[i][0]))
# #     for j in range(len(jb)):
# #         sheet.write(j+1,i,"{}".format(jb[j][i]))
# # f.save('bk.xls')
# ######################################################3
# # #/user/lib/env python
# # #--*-- conding= utf-8 -*-
# # import pymysql
# # with open('q.txt','r',encoding='utf8') as f:
# #     r=f.readlines()
# # abc=pymysql.connect(host='192.168.0.187',
# #                     port=3306,
# #                     user='root',
# #                     password='686789',
# #                     charset='utf8')
# # aaa=abc.cursor()
# # aaa.execute('show databases;')
# # aaa.execute('use py1')
# # aaa.execute('create table bkk(学号 int,姓名 char(20),年龄 int)')
# # aaa.execute('desc bk')
# # for i in r:
# #     i=i.split(' ')
# #     aaa.execute('insert into bkk values("{}","{}","{}")'.format(i[0],i[1],i[2]))
# # aaa.execute('select * from bkk')
# # print(aaa.fetchall())
# #######################################################3
# #     豆瓣爬虫
# # import requests
# # import re
# # import xlwt
# # class Shuming(object):
# #     def qingqiu(self,page):
# #         url='https://book.douban.com/top250?start={}'.format(page)
# #         head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
# #         response=requests.get(url=url,headers=head)
# #         html=response.content.decode('utf-8')
# #         # print(html)
# #         return html
# #     def guolv(self,html):
# #         mu=[]
# #         patt=re.compile('<td valign="top">(.*?)</td>',re.S)
# #         ptt=patt.findall(html)
# #         # print(ptt)
# #         for i in ptt:
# #
# #             itmes=re.findall('title="(.*?)"',i)
# #             #print(itmes)
# #             if itmes!='可试读':
# #                mu.append(itmes[0])
# #         print(mu)
# #         return mu
# #     def guolvj(self,htm):
# #         jian=[]
# #         patt = re.compile('<td valign="top">(.*?)</td>', re.S)
# #         ptt = patt.findall(htm)
# #         # print(ptt)
# #         for j in ptt:
# #             # print(j)
# #             patt2 =re.compile('<span class="inq">(.*?)</span>', re.S)
# #             itmes2 = patt2.findall(j)
# #             #print(itmes2)
# #             if len(itmes2)==0:
# #                 jian.append('没有')
# #             else:
# #                 jian.append(itmes2)
# #         print(jian)
# #         return jian
# #     def save(self,mu,jian):
# #         f=xlwt.Workbook()
# #         sheet=f.add_sheet('shuming')
# #         sheet.write(0,0,'书名')
# #         sheet.write(0,1,'简介')
# #         for i in range(len(mu)):
# #             sheet.write(i+1,0,mu[i])
# #         for j in range(len(jian)):
# #             sheet.write(j+1,1,jian[j])
# #         f.save('shudan.xls')
# #
# # s=Shuming()
# # a=s.qingqiu(0)
# # mu=s.guolv(a)
# # jian=s.guolvj(a)
# # s.save(mu,jian)
# #############################################################################################
# #爬小说
#
# # import requests
# # import re
# #
# # class Sheng(object):
# #     head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
# #     def qingqiu(self,page):
# #         url='http://www.ranwenxs.net/shu/3719/{}.html'.format(2780135+page)
# #         print(url)
# #         response=requests.get(url=url,headers=self.head)
# #         html=response.content.decode('gbk')
# #         # print(html)
# #         return html
# #     def guolv(self,html):
# #         pt=re.compile(r'<h1>(.*?)</h1>')
# #         itm=pt.findall(html)
# #         mu=itm[0]
# #         print(mu)
# #         patt=re.compile(r'&nbsp;&nbsp;&nbsp;&nbsp;(.*?)</div>',re.S)
# #         itmes=patt.findall(html)
# #         for i in itmes:
# #             i=i.replace('&nbsp;','').replace('<br />','')
# #             i=i.strip()
# #             return mu+'\n'+'\n'+'\n'+i+'\n'+'\n'
# #     def save(self,yong):
# #
# #         with open('圣墟.txt','a',encoding='utf-8') as f:
# #             f.write(yong)
# #
# # s=Sheng()
# # for ii in range(730,1270):
# #     a=s.qingqiu(ii)
# #     try:
# #         n=s.guolv(a)
# #         s.save(n)
# #     except:
# #         print()
# ############################################################################################
# ####################################################################################################
# ################################################################################################333333
# # import requests
# # import re
# # import xlwt
# # from xlutils.copy import copy
# # class Zuoan(object):
# #     head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
# #     def qingqiu(self,page):
# #         url='http://www.zreading.cn/page/{}'.format(page)
# #         respones=requests.get(url=url,headers=self.head)
# #         html=respones.content.decode('utf-8')
# #         # print(html)
# #         return html
# #     def guolv(self,html):
# #         mu=[]
# #         jian=[]
# #         tu=[]
# #         patt=re.compile('rel="bookmark(.*?)<footer class="block-footer u-clearfix">',re.S)
# #         html2=patt.findall(html)
# #         # print(html2)
# #         for i in html2:
# #             # print(i)
# #             patt1=re.compile('">(.*?)</a>',re.S)
# #             mu1=patt1.findall(i)
# #             mu.append(mu1[0])
# #             patt2=re.compile('</div>(.*?)</div>',re.S)
# #             jian1=patt2.findall(i)
# #             if len(jian1)==0:
# #                 jian.append('无简介')
# #             else:
# #                 jian.append(jian1[0])
# #             patt3=re.compile('background-image:url(.*?)">')
# #             tu1=patt3.findall(i)
# #             if len(tu1)==0:
# #                 tu.append('无图片')
# #             else:
# #                 tu1=tu1[0].replace('(','').replace(')','')
# #                 tu.append(tu1)
# #         #     print(tu1)
# #         # print(len(mu))
# #         # print(len(jian))
# #         # print(len(tu))
# #         return list(zip(mu,jian,tu))
# # ###################################################################################
# # #写入txt文件
# #     # def save(self,lis):
# #     #     for j in range(len(lis)):
# #     #         print(lis[j][0][0])
# #     #         with open('a.txt','a',encoding='utf-8') as f:
# #     #             f.write('******************'+lis[j][0]+'***************'+'\n')
# #     #             f.write(lis[j][2]+'\n')
# #     #             f.write(lis[j][1]+'\n'+'\n')
# #     #             try:
# #     #                 respones=requests.get(url=lis[j][2],headers=self.head)
# #     #                 html=respones.content
# #     #                 with open(r'{}.jpg'.format(j),'wb') as d:
# #     #                     d.write(html)
# #     #             except:
# #     #                 print()
# # ################################################################################
# # #导入EXCEL
# #     def save(self,lis):
# #         f=xlwt.Workbook('utf-8')
# #         sheet=f.add_sheet('shudan1')
# #         sheet.write(0, 0, '目录')
# #         sheet.write(0, 1, '图片')
# #         sheet.write(0, 2, '简介')
# #         for i in range(3):
# #             for j in range(len(lis)):
# #                 # print(lis)
# #                 # print(lis[j][0])
# #                 sheet.write(j+1,i,'{}'.format(lis[j][i]))
# #         f.save('pa.xls')
# # zuo=Zuoan()
# # guo=zuo.qingqiu(1)
# # lis=zuo.guolv(guo)
# # zuo.save(lis)
# ################################################################################################
# ############################################################################################
# #################################################################################################
# #txt   导入excel
# # import xlwt
# # neirong=[]
# # with open('q.txt','r',encoding='utf-8') as f:
# #     read=f.readlines()
# # for i in read:
# #     i=i.split(' ')
# #     neirong.append(i)
# # ff=xlwt.Workbook('utf-8')
# # sheet=ff.add_sheet('txt.xls')
# # sheet.write(0,0,'学号')
# # sheet.write(0,1,'名字')
# # sheet.write(0,2,'座位号')
# # for j in range(3):
# #     for i in range(len(neirong)):
# #         sheet.write(i+1,j,neirong[i][j])
# # ff.save('t.xls')
# ##################################################
# import pymysql
# import xlwt
# import xlrd
# # f=xlrd.open_workbook('bk.xls')
# # sheet=f.sheets()[0]
# # hang=sheet.nrows
# # lie=sheet.ncols
# # print(hang,lie)
# # with open('aa.txt','w',encoding='utf-8') as f:
# #     for i in range(31):
# #         n=sheet.row_values(i)
# #         f.write(n[0]+'  ')
# #         f.write(n[1]+'  ')
# #         f.write(str(n[2]))
# #         f.write('\n')
# # abc=pymysql.connect(host='192.168.0.187',
# #                     port=3306,
# #                     user='root',
# #                     password='686789')
# # aaa=abc.cursor()
# # # aaa.execute('create database py;')
# # aaa.execute('show databases')
# # aaa.execute('use py')
# # # aaa.execute('create table day1(学号 int,姓名 char(20),座位号 int)')
# # # aaa.execute('show tables')
# # # with open('aa.txt','r',encoding='utf-8') as fff:
# # #     q=fff.readlines()
# # #     for j in range(len(q)-1):
# # #         print(q[j+1])
# # #         i=q[j+1].split('  ')
# # #         print(i)
# # #         aaa.execute('insert into day1 values("{}","{}","{}")'.format(int(i[0]),i[1],i[2]))
# # aaa.execute('select * from day1')
# # print(aaa.fetchall())
# ##############################################################################################          哈哈
# import pymysql
# import xlrd
# # abc=pymysql.connect(host='192.168.0.187',
# #                     port=3306,
# #                     user='root',
# #                     password='686789',
# #                     charset='utf8')
# # aaa=abc.cursor()
# # aaa.execute('show databases;')
# # aaa.execute('use py')
# # aaa.execute('show tables')
# # aaa.execute('select * from day1')
# # ku=aaa.fetchall()
# # aaa.execute('desc day1;')
# # tou=aaa.fetchall()
# # with open('ax.txt','w',encoding='utf-8') as f:
# #     f.write('{},{},{}'.format(tou[0][0],tou[1][0],tou[2][0]))
# #     f.write('\n')
# #     for i in ku:
# #         f.write('{},{},{}'.format(i[0],i[1],i[2]))
# #         f.write('\n')
#
# # with open('ax.txt','r',encoding='utf-8') as f:
# #     neirong=f.readlines()
# # ff=xlwt.Workbook('utf-8')
# # sheet=ff.add_sheet('txt.xls')
# # for j in range(3):
# #     for i in range(len(neirong)):
# #         sheet.write(i,j,'{}'.format(neirong[i].split(',')[j]))
# # ff.save('txtt.xls')
# #
# # import xlwt
# # import xlrd
# # import pymysql
# # abc=pymysql.connect(host='192.168.0.187',
# #                     port=3306,
# #                     user='root',
# #                     password='686789',
# #                     charset='utf8'
# #                     )
# # aaa=abc.cursor()
# # aaa.execute('show databases;')
# # print(aaa.fetchall())
# # import requests
# # import re
# # class qianqian(object):
# #     head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
# #     def qingqiu(self):
# #         url='https://www.qianqianhua.com/fengjing/2794.html'
# #         respones=requests.get(url=url,headers=self.head)
# #         html=respones.content.decode('utf-8')
# #         # print(html)
# #         return html
# #     def guolv(self,html):
# #         patt=re.compile('align="center"><img src="(.*?)"')
# #         itmes=patt.findall(html)
# #         # print(itmes)
# #         return itmes
# #     def save(self,tu):
# #         j=0
# #         for i in tu:
# #             print(i)
# #             qing=requests.get(url=i,headers=self.head)
# #             html=qing.content
# #             with open(r'C:\Users\LIU\Desktop\地理中国\{}.jpeg'.format(j),'wb') as f:
# #                 f.write(html)
# #                 j+=1
# # qian=qianqian()
# # html=qian.qingqiu()
# # tu=qian.guolv(html)
# # qian.save(tu)
#
# # import requests
# # import re
# # class qianqian():
# #     head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
# #     def qingqiu(self):
# #         url='https://www.qianqianhua.com'
# #         respones=requests.get(url=url,headers=self.head)
# #         html=respones.content.decode('utf-8')
# #         return html
# #     def mulu(self,html):
# #         mu=[]
# #         patt=re.compile('<ul class="nav clearfix">(.*?)</ul>',re.S)
# #         itmes=patt.findall(html)
# #         itmes=itmes[0]
# #         itmes=itmes.replace('<li><a  href="','').replace('">','  ').replace('</a></li>','')
# #         print(itmes)
# #     def zi(self):
# #         lei=input('>>>>>>>>>')
# #         url='https://www.qianqianhua.com/{}/'.format(lei)
# #         response=requests.get(url=url,headers=self.head)
# #         zihtml=response.content.decode('utf-8')
# #         return zihtml
# #     def ziguolv(self,zihtml):
# #         patt=re.compile('<div class="tit"><a href="(.*?)"',re.S)
# #         html=patt.findall(zihtml)
# #         print(len(html))
# #         print(type(html))
# #         return html
# #     def zitu(self,html):
# #         mingzi=2000
# #         for ii in range(len(html)):
# #             bb = 1
# #             iiii = 0
# #             while True:
# #                 try:
# #                     print('sdfsd')
# #                     # https: // www.qianqianhua.com / fengjing / 86403.html
# #                     # https: // www.qianqianhua.com / fengjing / 86403_2.html
# #                     url = html[ii].replace('.h','_{}.h'.format(iiii+1))
# #                     print(url)
# #                     responese = requests.get(url=url, headers=self.head)
# #                     zhtml = responese.content.decode('utf-8')
# #                     ptt = re.compile('</span> </h2><p><img src="(.*?)" /></p></p>', re.S)
# #                     zihtml = ptt.findall(zhtml)
# #                     for i in zihtml:
# #                         pt = re.compile('http(.*?)"', re.S)
# #                         ziip = pt.findall(zihtml[0])
# #                         for j in ziip:
# #                             url = 'http' + j
# #                             res = requests.get(url=url, headers=self.head)
# #                             ht = res.content
# #                             with open(r'C:\Users\LIU\Desktop\地理中国\{}.jpg'.format(mingzi), 'wb') as fff:
# #                                 fff.write(ht)
# #                             mingzi += 1
# #                     iiii += 1
# #                 except:
# #                     bb+=1
# #                     print(bb)
# #                     print(bb)
# #                     if bb<3:
# #                         url = html[ii]
# #                         responese = requests.get(url=url, headers=self.head)
# #                         zhtml = responese.content.decode('utf-8')
# #                         ptt = re.compile('</span> </h2><p><img src="(.*?)" /></p></p>', re.S)
# #                         zihtml = ptt.findall(zhtml)
# #                         for i in zihtml:
# #                             pt = re.compile('http(.*?)"', re.S)
# #                             ziip = pt.findall(zihtml[0])
# #                             for j in ziip:
# #                                 url = 'http' + j
# #                                 res = requests.get(url=url, headers=self.head)
# #                                 ht = res.content
# #                                 with open(r'C:\Users\LIU\Desktop\地理中国\{}.jpg'.format(mingzi), 'wb') as fff:
# #                                     fff.write(ht)
# #                                 mingzi += 1
# #                     else:
# #                         break
# #                     iiii += 1
# #             # finally:
# #             #     for i in zihtml:
# #             #         pt = re.compile('http(.*?)"', re.S)
# #             #         ziip = pt.findall(zihtml[0])
# #             #         for j in ziip:
# #             #             url = 'http' + j
# #             #             res = requests.get(url=url, headers=self.head)
# #             #             ht = res.content
# #             #             with open(r'C:\Users\LIU\Desktop\地理中国\{}.jpg'.format(mingzi), 'wb') as fff:
# #             #                 fff.write(ht)
# #             #             mingzi += 1
# #             #
# #             #
# #             #
# #             #
# #             #     print(ziip)
# #             # break
# #
# # qian=qianqian()
# # mu=qian.qingqiu()
# # qian.mulu(mu)
# # zimu=qian.zi()
# # html=qian.ziguolv(zimu)
# # qian.zitu(html)
# #￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥4￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥
#
# # a=['qw','a','b','A','B']
# # a.sort()
# # print(a)
#
# # print(ord('a'))
# # print(chr(97))
# # print(ord('8'))
#
# #
# #
# # import requests
# # import re
# # class pachong(object):
# #     head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36' }
# #     def qing(self,page):
# #         url='https://www.doutula.com/article/list/?page={}'.format(page)
# #         print(url)
# #         reponese=requests.get(url=url,headers=self.head)
# #         html=reponese.content.decode('utf-8')
# #         # print(html)
# #         return html
# #     def guolv(self,html):
# #         patt=re.compile('</div> <div class="col-sm-9">(.*?)<div class="text-center">',re.S)
# #         itmes=patt.findall(html)
# #         patt1=re.compile('<a href="(.*?)"',re.S)
# #         itme1=patt1.findall(itmes[0])
# #         # print(itme1)
# #         return itme1
# #     def ziqing(self,itme1):
# #         ht=[]
# #         for i in itme1:
# #             # print(i)
# #             responese=requests.get(url=i,headers=self.head)
# #             html=responese.content.decode('utf-8')
# #             # print(html)
# #             ht.append(html)
# #         # print(ht)
# #         # print(len(ht))
# #         return ht
# #     def ziguo(self,ht,htt):
# #         jia=0
# #         for i in ht:
# #             patt=re.compile("this.src='(.*?)'")
# #             zguo=patt.findall(i)
# #             for j in zguo:
# #                 print(type(j))
# #                 print(j[-4:])
# #                 reponses=requests.get(url=j,headers=self.head)
# #                 html=reponses.content
# #                 with open(r'C:\Users\LIU\Desktop\python\表情包\{}_{}.{}'.format(htt,jia,j[-4:]),'wb') as f:
# #                     f.write(html)
# #                 jia+=1
# #                 print(jia)
# #
# # aa=pachong()
# # for i in range(17,18):
# #     htm=aa.qing(i)
# #     itmes=aa.guolv(htm)
# #     zq=aa.ziqing(itmes)
# #     aa.ziguo(zq,i)
# ##################################################################################
# # import xlwt
# # with open('aa.txt','r',encoding='utf-8') as f:
# #     a=f.readlines()
# #     print(a)
# # ff=xlwt.Workbook()
# # sheet=ff.add_sheet('lianxi')
# # for i in range(3):
# #     for j in range(len(a)):
# #         sheet.write(j,i,'{}'.format(a[j].split('  ')[i]))
# # ff.save('awe.xls')
# #
# # import xlrd
# # import pymysql
# # abx=pymysql.connect(host='192.168.0.187',
# #                     port=3306,
# #                     user='root',
# #                     password='686789',
# #                     charset='utf8')
# # aa=abx.cursor()
# # aa.execute('show databases')
# # aa.execute('use py')
# # aa.execute('show tables')
# # aa.execute('select * from day1')
# # # aa.execute('create table day2(学号 int,姓名 char(20),班级 int)')
# # aa.execute('show tables')
# # f=xlrd.open_workbook('awe.xls')
# # sheet=f.nsheets
# # sheet1=f.sheets()[0]
# # hang=sheet1.nrows
# # lie=sheet1.ncols
# # # for i in range(1,hang):
# # #     n=sheet1.row_values(i)
# # #     print(n)
# # #     aa.execute("insert into day2 values('{}','{}','{}')".format(n[0],n[1],n[2]))
# # aa.execute('select * from day2')
# # aa.execute('desc day2')
# # print(aa.fetchall())
# # import pymysql
# # import xlwt
# # abc=pymysql.connect(host='192.168.0.187',
# #                     port=3306,
# #                     user='root',
# #                     password='686789',
# #                     charset='utf8')
# # aa=abc.cursor()
# # aa.execute('show databases')
# # aa.execute('use py')
# # aa.execute('select * from day2')
# # nei=aa.fetchall()
# # # print(nei)
# # aa.execute('desc day2')
# # biao=aa.fetchall()
# # # print(biao[0][0],biao[1][0],biao[2][0])
# # # print(aa.fetchall())
# # f=xlwt.Workbook('utf-8')
# # sheet=f.add_sheet('kd')
# # for i in range(3):
# #     print(biao)
# #     sheet.write(0,i,'{}'.format(biao[i][0]))
# #     for j in range(len(nei)-1):
# #         sheet.write(j+1,i,'{}'.format(nei[j][i]))
# # f.save('kudao.xls')
# # import pymysql
# # import xlrd
# # f=xlrd.open_workbook('kudao.xls')
# # sheet=f.nsheets
# # sheet1=f.sheets()[0]
# # hang=sheet1.nrows
# # lie=sheet1.ncols
# # print(hang,lie)
# # abc=pymysql.connect(host='192.168.0.187',
# #                     port=3306,
# #                     user='root',
# #                     password='686789',
# #                     charset='utf8')
# # aa=abc.cursor()
# # aa.execute('use py')
# # # aa.execute('create table day2_2({} int,{} char(20),{} int )'.format(sheet1.row_values(0)[0],sheet1.row_values(0)[1],sheet1.row_values(0)[2]))
# # # aa.execute('show tables')
# # # print(aa.fetchall())
# # # for i in range(1,hang):
# # #     n=sheet1.row_values(i)
# # #     aa.execute('insert into day2_2 values("{}","{}","{}")'.format(n[0],n[1],n[2]))
# # # abc.commit()
# # aa.execute('select * from day2_2')
# # print(aa.fetchall())
#
# # import xlrd
# # f=xlrd.open_workbook('kudao.xls')
# # sheet=f.nsheets
# # sheet1=f.sheets()[0]
# # hang=sheet1.nrows
# # lie=sheet1.ncols
# # print(hang,lie)
# # with open('bdt.txt','w',encoding='utf-8') as f:
# #     for i in range(hang):
# #         for j in range(lie):
# #             nei=sheet1.row_values(i)
# #             f.write(nei[j])
# #             if j<2:
# #                 f.write(' , ')
# #         f.write('\n')
#
# ##################################################################
# # import requests
# # import re
# # class che():
# #     head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
# #     def qing(self,page):
# #         if page>1:
# #             url='http://pic.netbian.com/4kqiche/index_{}.html'.format(page)
# #         elif page==1:
# #             url = 'http://pic.netbian.com/4kqiche/index.html'
# #         res=requests.get(url=url,headers=self.head)
# #         html=res.content.decode('gbk')
# #         return(html)
# #     def guolv(self,html):
# #         patt=re.compile('<ul class="clearfix">(.*?)</ul>',re.S)
# #         itmes=patt.findall(html)
# #         patt1=re.compile('<img src="(.*?)"',re.S)
# #         itmes1=patt1.findall(itmes[0])
# #         # print(itmes1)
# #         return itmes1
# #     def save(self,itmes1,ye):
# #         print(ye)
# #         zhang=0
# #         for i in itmes1:
# #             url='http://pic.netbian.com'+i
# #             # print(url)
# #             res=requests.get(url=url,headers=self.head)
# #             itmes=res.content
# #             # print(itmes)
# #             with open(r'C:\Users\LIU\Desktop\地理中国\che{}_{}.{}'.format(ye,zhang,url[-3:]),'wb') as f:
# #                 f.write(itmes)
# #             zhang+=1
# # a = che()
# # for i in range(1,8):
# #     q = a.qing(i)
# #     g = a.guolv(q)
# #     a.save(g,i)
# #
#
#
#
# ################################################################3
# # import os
# # # for i in range(10):
# # #     os.mkdir(r'C:\Users\LIU\Desktop\地理中国\{}'.format(i))
# # #     a=r'C:\Users\LIU\Desktop\地理中国\{}'.format(i)
# # #     with open(r'{}\a.txt'.format(a), 'w', encoding='utf-8') as f:
# # #         for j in range(5):
# # #             f.write('jkdfdskjfhfsdkfl'+'\n')
# # #     os.remove(r'{}\a.txt'.format(a))
# # #     os.rmdir(i)
# #
# # ###############################################################333
# # # import xlrd
# # # f=xlrd.open_workbook('kudao.xls')
# # # sheet=f.nsheets
# # # sheet1=f.sheets()[0]
# # # hang=sheet1.nrows
# # # lie=sheet1.ncols
# # # read=sheet1.row_values(0)
# # # with open('aa.txt','w',encoding='utf-8') as fe:
# # #     fe.write('{}'.format(read))
# # # # print(sheet,hang,lie,len(read))
# # # import xlrd
# # # from xlutils.copy import copy
# # # f=xlrd.open_workbook('awe.xls')
# # # new_f=copy(f)
# # # sheet=new_f.get_sheet(0)
# # # sheet.write(7,7,'7777777')
# # # new_f.save('awe.xls')
# #
# # # import os
# # # print(os.getcwd())
# # # os.rename('s_socke.py','socket_server.py')
# #
# # from tkinter import *
# # from tkinter import messagebox
# # from PIL import Image
# # from PIL import ImageTk
# # # # 创建窗口
# # window = Tk()
# # #定义窗口标题
# # window.title('hello')
# # #设置窗口大小
# # window.geometry('400x400')
# # #定义文本标签
# # # wd=Label(window,text='nihao',font=('微软雅黑',20))
# # # #将标签放在窗口那个位置
# # # wd.grid(row=0,column=0)  #行    列
# # # #定义一个按钮
# # # # bu=
# # # # # 显示窗口
# # window=mainloop()
#
# # q=chr(68)
# # print(q)
# # w=ord('D')
# # print(w)
# import os
# # os.remove('aa.txt')
# # import xlrd
# # f=xlrd.open_workbook('awe.xls')
# # sheet=f.nsheets
# # sheet1=f.sheets()[0]
# # hang=sheet1.nrows
# # lie=sheet1.ncols
# # print(hang,lie)
# # with open('aa.txt','w',encoding='utf-8') as f:
# #     for j in range(hang):
# #         neirong=sheet1.row_values(j)
# #         print(neirong)
# #         for i in range(lie):
# #             if i<lie-1:#                 f.write(neirong[i]+',')
# #             else:
# #                 f.write(neirong[i])
#
# # import xlwt
# # with open('aa.txt','r',encoding='utf-8')as f:
# #     liebiao=f.readlines()
# # f=xlwt.Workbook()
# # sheet=f.add_sheet('asd')
# # for i in range(len(liebiao)):
# #     for j in range(len(liebiao[0].split(','))):
# #         sheet.write(i,j,'{}'.format(liebiao[i].split(',')[j]))
# #     f.save('qwe.xls')
#
#
# # import pymysql
# # abc=pymysql.connect(host='192.168.0.187',
# #                     port=3306,
# #                     user='root',
# #                     password='686789',
# #                     charset='utf8')
# # aaa=abc.cursor()
# # aaa.execute('show databases')
# # aaa.execute('use py')
# # aaa.execute('show tables')
# # #aaa.execute('create table day3(学号 int,姓名 char(20),年级 int)')
# # aaa.execute('desc day3')
# # with open('aa.txt','r',encoding='utf-8') as f:
# #     nei=f.readlines()
# # for i in range(1,len(nei)):
# #     aaa.execute('insert into day3 values("{}","{}","{}")'.format(nei[i].split(',')[0],nei[i].split(',')[1],nei[i].split(',')[2]))
# # aaa.execute('select * from day3')
# # print(aaa.fetchall())
#
# # import pymysql
# # abc=pymysql.connect(host='192.168.0.187',port=3306,user='root',password='686789',charset='utf8')
# # aa=abc.cursor()
# # aa.execute('show databases')
# # aa.execute('use py')
# # aa.execute('show tables')
# # aa.execute('select * from day3')
# # nei=aa.fetchall()
# # aa.execute('desc day3')
# # tou=aa.fetchall()
# # with open('as.txt','w',encoding='utf-8')as f:
# #     f.write('{},{},{}'.format(tou[0][0],tou[1][0],tou[2][0])+'\n')
# #     for i in nei:
# #         print(i)
# #         f.write('{},{},{}'.format(i[0],i[1],i[2])+'\n')
# # # print(aa.fetchall())4
# #
# # import pymysql
# # abc=pymysql.connect(host='192.168.0.187',port=3306,user='root',password='686789',charset='utf8')
# # aa=abc.cursor()
# # aa.execute('show databases')
# # print(aa.fetchall())
# import os
# os.remove('qwe.xls')
# os.remove('xx.xls')
# os.remove('txt.xls')
# import os
# os.remove('awe.xls')
# import xlwt
# with open('a.txt','r',encoding='utf-8') as f:
#     nei=f.readlines()
#     # print(nei)
# ff=xlwt.Workbook()
# sheet=ff.add_sheet('rtr')
# for i in range(len(nei)):
#     ii=nei[i].split(',')
#     print(ii)
#     for j in range(len(ii)):
#         dd=ii[j]
#         print(dd)
#         sheet.write(i,j,'{}'.format(dd))
# ff.save('awe.xls')

#
# import os
# os.remove('aa.txt')

# import xlrd
# f=xlrd.open_workbook('awe.xls')
# biao=f.nsheets
# print(biao)
# sheet=f.sheets()[0]
# hang=sheet.nrows
# lie=sheet.ncols
# print(hang,lie)
# with open('aa.txt','w',encoding='utf-8') as ff:
#     for i in range(hang):
#         for j in range(len(sheet.row_values(i))):
#             if j<len(sheet.row_values(i))-1:
#                 ff.write('{}'.format(sheet.row_values(i)[j])+',')
#             else:
#                 ff.write('{}'.format(sheet.row_values(i)[j]))
# import xlrd
# from xlutils.copy import copy
# f=xlrd.open_workbook('awe.xls')
# new_f=copy(f)
# sheet=new_f.get_sheet(0)
# sheet.write(10,10,'sdfghjklkjhgfdfghj')
# new_f.save('aaww.xls')
# import pymysql
# abc=pymysql.connect(host='192.168.0.187',user='root',port=3306,password='686789',charset='utf8')
# aa=abc.cursor()
# aa.execute('show databases')
# aa.execute('use py')
# aa.execute('show tables')
# with open('a.txt','r',encoding='utf-8') as f:
#     nei=f.readlines()
# # print(nei)
# # aa.execute('create table day5(学号 int,姓名 char(10),年级 int)')
# aa.execute('desc day5')
# for i in range(1,len(nei)):
#     aa.execute('insert into day5 values("{}","{}","{}")'.format(nei[i].split(',')[0],nei[i].split(',')[1],nei[i].split(',')[2]))
# abc.commit()
# import pymysql
# import xlrd
# abc=pymysql.connect(host='192.168.0.187',user='root',password='686789',port=3306,charset='utf8')
# aa=abc.cursor()
# aa.execute('show databases')
# aa.execute('use py')
# f=xlrd.open_workbook('awe.xls')
# shu=f.nsheets
# sheet=f.sheets()[0]
# hang=sheet.nrows
# lie=sheet.ncols
# print(hang,lie,shu)
# # aa.execute('create table day5_2(学号 int,姓名 char(20),年级 int)')
# # for i in range(1,hang):
# #     nei=sheet.row_values(i)
# #     print(type(nei))
# #     aa.execute('insert into day5_2 values("{}","{}","{}")'.format(nei[0],nei[1],nei[2]))
# # abc.commit
# aa.execute('select * from day5_2')
# print(aa.fetchall())
# import pymysql
# import xlwt
# abc=pymysql.connect(host='192.168.0.187',port=3306,user='root',password='686789',charset='utf8')
# aa=abc.cursor()
# aa.execute('use py')
# aa.execute('select * from day5_2')
# nei=aa.fetchall()
# f=xlwt.Workbook()
# sheet=f.add_sheet('sadfks')
# aa.execute('desc day5_2')
# tou=aa.fetchall()
# for q in range(len(tou)):
#     sheet.write(0,q,'{}'.format(tou[q][0]))
# for i in range(1,len(nei)):
#     for j in range(len(nei[i])):
#         sheet.write(i,j,'{}'.format(nei[i][j]))
# f.save('asd.xls')
# # import os
# # os.remove('asd.xlks')

# import pymysql
# abc=pymysql.connect(host='192.168.0.187',user='root',password='686789',port=3306,charset='utf8')
# aa=abc.cursor()
# aa.execute('use py')
# aa.execute('show tables')
# aa.execute('select * from day5_2')
# nei=aa.fetchall()
# print(nei)
# aa.execute('desc day5_2')
# tou=aa.fetchall()
# print(tou[0][0])
# with open('aqw.txt','w',encoding='utf-8') as f:
#     f.write('{},{},{}'.format(tou[0][0],tou[1][0],tou[2][0]+'\n'))
#     for i in range(len(nei)):
#         for j in range(len(nei[i])):
#             if j<len(nei[i])-1:
#                 f.write('{}'.format(nei[i][j])+',')
#             else:
#                 f.write('{}'.format(nei[i][j])+'\n')


import smtplib
import email.mime.text
import  email.mime.multipart
sender='17839210919@163.com'
recover='1873362204@qq.com'
server='smtp.163.com'
passwd='LYY686789'
message=email.mime.multipart.MIMEMultipart()
message['from']=sender
message['to']=recover
message['subject']='主题'
text="""sdfsdf
dsfsdfs
sdfsdfs
sdfsdf"""
text=email.mime.text.MIMEText(text)
message.attach(text)
smtp123=smtplib.SMTP_SSL(server,465)
smtp123.login(sender,passwd)
smtp123.sendmail(sender,recover,message.as_string())
smtp123.close()


