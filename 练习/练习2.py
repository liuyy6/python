# import requests
# import re
# class boke(object):
#     def qing(self):
#         url='https://blog.csdn.net/nanggong/article/details/23295293'
#         head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
#         response=requests.get(url=url,headers=head)
#         html=response.content.decode('utf-8')
#         # print(html)
#         return html
#     def guolv(self,html):
#         guo=[]
#         patt=re.compile('<div class="htmledit_views">(.*?)</div>',re.S)
#         itmes=patt.findall(html)
#         itmes=itmes[0].replace(' ','').replace('<span>','').replace('<p></span>','').replace('</p><p></span>',',').replace('</p>','')
#         print(itmes)
#         return itmes
#     def save(self,itmes):
#         with open('a.txt','w',encoding='utf-8') as f:
#             f.write(itmes)
# aa=boke()
# gg=aa.qing()
# jj=aa.guolv(gg)
# aa.save(jj)

###################################################################################
# import xlwt
# with open('aa.txt','r',encoding='utf-8') as f:
#     nei=f.readlines()
# f=xlwt.Workbook()
# sheet=f.add_sheet('txt')
# for i in range(3):
#     for j in range(len(nei)):
#         sheet.write(j,i,'{}'.format(nei[j].split(',')[i]))
# f.save('txt.xls')

# import xlrd
# f=xlrd.open_workbook('txt.xls')
# sheet=f.nsheets
# sheet1=f.sheets()[0]
# hang=sheet1.nrows
# lie=sheet1.ncols
# print(hang,lie)
# with open('xls.txt','w',encoding='utf-8') as ff:
#     for j in range(hang):
#         nei=sheet1.row_values(j)
#         for i in range(lie):
#             if i<lie-1:
#                 ff.write('{}'.format(nei[i])+',')
#             else:
#                 ff.write('{}'.format(nei[i]))
# import requests
# import re
# url='https://bbs.csdn.net/topics/390505050'
# head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36' }
# res=requests.get(url=url,headers=head)
# html=res.content.decode('utf-8')
# # print(html)
# patt=re.compile(' <div class="post_body post_body_min_h">(.*?)<div marginwidth="0" marginheight="0" scrolling="no" width="100%">',re.S)
# itmes=patt.findall(html)
# print(len(itmes))
# itmes=itmes[0].replace('<br />','').replace('&nbsp;&nbsp;&nbsp;&nbsp;','\n')
# print(itmes)
# with open('qq.txt','w',encoding=('utf-8')) as fff:
#     fff.write(itmes)
# import os
# os.remove('qq.xls')

# import pymysql
# abc=pymysql.connect(host='192.168.0.187',port=3306,user='root',password='686789',charset='utf8')
# aa=abc.cursor()
# aa.execute('show databases')
# aa.execute('use py')
# aa.execute('show tables')
# aa.execute('select * from day3')
# nei=aa.fetchall()
# aa.execute('desc day3')
# tou=aa.fetchall()
# with open('ww.txt','w',encoding='utf-8') as w:
#     for  j in range(len(tou)):
#         w.write('{}'.format(tou[j][0]))
#     w.write('\n')
#     for i in range(len(nei)):
#         for u in range(len(nei[i])):
#             if u<len(nei[i])-1:
#                 w.write('{}'.format(nei[i][u])+',')
#             else:
#                 w.write('{}'.format(nei[i][u]))
#         w.write('\n')




# import pymysql
# abc=pymysql.connect(host='192.168.0.187',user='root',password='686789',port=3306,charset='utf8')
# aa=abc.cursor()
# aa.execute('show databases')
# aa.execute('use py')
# aa.execute('show tables')
# aa.execute('create table day3_2(学号 int,姓名 char(20),年级 int)')
# aa.execute('desc day3_2')
# tou=aa.fetchall()
# with open('aa.txt','r',encoding='utf-8')as f:
#     ff=f.readlines()
# print(ff)
# for i in range(1,len(ff)):
#     f1=ff[i].split(',')
#     aa.execute('insert into day3_2 values("{}","{}","{}")'.format(f1[0],f1[1],f1[2]))
# abc.commit()


# import xlrd
# import pymysql
# f=xlrd.open_workbook('txt.xls')
# sheet=f.sheets()[0]
# hang=sheet.nrows
# lie=sheet.ncols
# abc=pymysql.connect(host='192.168.0.187',user='root',port=3306,password='686789',charset='utf8')
# aa=abc.cursor()
# aa.execute('use py')
# # aa.execute('create table day4(学号 int,姓名 char(20),年级 int)')
# aa.execute('desc day4')
# print(aa.fetchall())
# for j in range(1,hang):
#     xx=sheet.row_values(j)
#     print(xx)
#     aa.execute('insert into day4 values("{}","{}","{}")'.format(xx[0],xx[1],xx[2]))

#
# import pymysql
# import xlwt
# abc=pymysql.connect(host='192.168.0.187',port=3306,user='root',password='686789',charset='utf8')
# aa=abc.cursor()
# aa.execute('use py ')
# aa.execute('select * from day4')
# nei=aa.fetchall()
# # print(nei)
# aa.execute('desc day4')
# tou=aa.fetchall()
# f=xlwt.Workbook()
# sheet=f.add_sheet('xx')
# for i in range(len(nei)):
#     for  j in range(len(tou)):
#         print(nei[i][j])
#         # sheet.write(0,0,'erty')
#         sheet.write(i,j,"{}".format(nei[i][j]))
# f.save('xx.xls')
#
# a='''nihaio
# asodko
# skdopsa
# dskod;'''
#
# import smtplib
# import email.mime.text
# import email.mime.multipart
# sender='17839210919@163.com'
# recver='1873362204@qq.com'
# server='smtp.163.com'
# passwd='LYY686789'
# message=email.mime.multipart.MIMEMultipart()
# message['from']=sender
# message['to']=recver
# message['subject']='主题'
# text=a
# text=email.mime.text.MIMEText(text)
# message.attach(text)
# smtp123=smtplib.SMTP_SSL(server,465)
# smtp123.login(sender,passwd)
# smtp123.sendmail(sender,recver,message.as_string())
# smtp123.close()
#####################
# import smtplib
# import email.mime.text
# import email.mime.multipart
# sender='17839210919@163.com'
# recver='1873362204@qq.com'
# server='smtp.163.com'
# passwd='LYY686789'
# message=email.mime.multipart.MIMEMultipart()
# message['from']=sender
# message['to']=recver
# message['subject']='zhuti'
# text='fghjkl'
# text=email.mime.text.MIMEText(text)
# message.attach(text)
# smtp123=smtplib.SMTP_SSL(server,465)
# smtp123.login(sender,passwd)
# smtp123.sendmail(sender,recver,message.as_string())
# smtp123.close()

# import smtplib
# import email.mime.text
# import email.mime.multipart
# sender='17839210919@163.com'
# recver='1873362204@qq.com'
# server='smtp.163.com'
# passwd='LYY686789'
# message=email.mime.multipart.MIMEMultipart()
# message['from']=sender
# message['t0']=recver
# message['subject']='zhuti'
# text="""sfsd
# sfdfsd
# f
# sdsd
# fds
# fdsf
# ds
# f"""
# text=email.mime.text.MIMEText(text)
# message.attach(text)
# smtp123=smtplib.SMTP_SSL(server,465)
# smtp123.login(sender,passwd)
# smtp123.sendmail(sender,recver,message.as_string())
# smtp123.close()
# import smtplib
# import email.mime.text
# import email.mime.multipart
# sender='17839210919@163.com'
# recver='1873362204@qq.com'
# server='smtp.163.com'
# passwd='LYY686789'
#
#
# import xlwt
# with open('aa.txt','r',encoding='utf-8')as f:
#     nei=f.readlines()
# print(nei)
# x=xlwt.Workbook(encoding='utf-8')
# sheet=x.add_sheet('txt')
# for i in range(len(nei)):
#     ii=nei[i].replace('\n','').split(',')
#     print(i)
#     for j in range(len(ii)):
#         sheet.write(i,j,'{}'.format(ii[j]))
#         print(j)
# ff.save('qa.xls')
#
# import xlrd
# f=xlrd.open_workbook('qwe.xls')
# sheet=f.sheets()[0]
# hang=sheet.nrows
# lie=sheet.ncols
# print(hang,lie)
# with open('a.txt','w',encoding='utf-8')as ff:
#     for i in range(hang):
#         nei=sheet.row_values(i)
#         for j in range(len(nei)):
#             if j<len(nei)-1:
#                 ff.write(nei[j]+',')
#             else:
#                 ff.write(nei[j])
# import os
# # os.remove('a.txt')
# import pymysql
# abc=pymysql.connect(host='192.168.0.187',port=3306,user='root',password='686789',charset='utf8')
# aa=abc.cursor()
# aa.execute('show databases')
# aa.execute('use py')
# # aa.execute('create table qw(学号 int,姓名 char(20),年级 int)')
# aa.execute('desc qw')
# with open('aa.txt','r',encoding='utf-8') as ff:
#     nei=ff.readlines()
# for i in range(1,len(nei)):
#     ne=nei[i].split(',')
#     aa.execute('insert into qw values("{}","{}","{}")'.format(ne[0],ne[1],ne[2]))
# abc.commit()
# # print(aa.fetchall())
#
# import pymysql
# abc=pymysql.connect(host='192.168.0.187',port=3306,user='root',password='686789',charset='utf8')
# aa=abc.cursor()
# aa.execute('use py')
# aa.execute('select * from day3')
# nei=aa.fetchall()
# aa.execute('desc day3')
# tou=aa.fetchall()
# with open('a.txt','w',encoding='utf-8')as f:
#     f.write('{},{},{}'.format(tou[0][0],tou[1][0],tou[2][0]))
#     f.write('\n')
#     for i in range(len(nei)):
#         for j in range(len(tou)):
#             if j<2:
#                 f.write(str(nei[i][j])+',')
#             else:
#                 f.write(str(nei[i][j]))
#         f.write('\n')
# # print(aa.fetchall())
# import os
# # os.remove('aa.txt')
# import xlrd
# import pymysql
# f=xlrd.open_workbook('awe.xls')
# ji=f.nsheets
# print(ji)
# sheet=f.sheets()[0]
# hang=sheet.nrows
# lie=sheet.ncols
# print(hang,lie)
# abc=pymysql.connect(host='192.168.0.187',port=3306,user='root',password='686789',charset='utf8')
# aa=abc.cursor()
# aa.execute('use py')
# # aa.execute('create table day4_2(学号 int,姓名 char(20),年级 int)')
# aa.execute('desc day4')
# for i in range(1,hang):
#     nei=sheet.row_values(i)
#     aa.execute('insert into day4_2 values("{}","{}","{}");'.format(nei[0],nei[1],nei[2]))
# abc.commit()
# print(aa.fetchall())
# a='({},{},{})'.format('sdf','sdf','sdfsd')
# print(a)

#
# import pymysql
# import xlwt
# abc=pymysql.connect(host='192.168.0.187',user='root',port=3306,password='686789',charset='utf8')
# aa=abc.cursor()
# aa.execute('show databases')
# # print('aa.fetchall')
# aa.execute('use py')
# aa.execute('select * from day4_2')
# nei=aa.fetchall()
# aa.execute('desc day4')
# tou=aa.fetchall()
# f=xlwt.Workbook()
# sheet=f.add_sheet('dsa')
# for j in range(len(tou)):
#     sheet.write(0,j,'{}'.format(tou[j][0]))
#     for i in range(1,len(nei)):
#         sheet.write(i,j,"{}".format(nei[i][j]))
# f.save('qq.xls')
# # sheet.write()
# print(aa.fetchall())


# import os
# os.remove('qq.xls')



# import requests
# import re
# class Pchong():
#     def qing(self,page):
#         url='https://www.qiushibaike.com/8hr/page/{}/'.format(page)
#         head={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
#         respones=requests.get(url=url,headers=head)
#         html=respones.content.decode('utf-8')
#         # print(html)
#         return(html)
#     def guolv(self,html):
#         shuju=[]
#         patt=re.compile('<div class="content">(.*?)</span>',re.S)
#         itmes=patt.findall(html)
#         for i in itmes:
#             itme=i.replace('<span>','').replace('\n','')+'\n'
#             shuju.append(itme)
#         return(shuju)
#     def save(self,item):
#         # print(item)
#         with open('aa.txt','w',encoding='utf-8') as f:
#             for j in item:
#                 # print(j)
#                 f.write(j+'\n')
# a=Pchong()
# html=a.qing(1)
# item=a.guolv(html)
# a.save(item)
# import smtplib
# import email.mime.text
# import email.mime.multipart
# sender='17839210919@163.com'
# recver='18733620204@qq.com'
# server='smtp.163.com'
# password='LYY686789'
# message=email.mime.multipart.MIMEMultipart()
# message['from']=sender
# message['to']=recver
# message['subject']='zhuti'
# text="""sdfds
# sdfsd
# fds
# dsf"""
# text=email.mime.text.MIMEText(text)
# message.attach(text)
# smtp123=smtplib.SMTP_SSL(server,465)
# smtp123.login(sender,password)
# smtp123.sendmail(sender,recver,message.as_string())
# smtp123.close()

import requests
import re
import os
class Doutu():
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    def qing(self,page):
        url='http://www.doutula.com/article/list/?page={}'.format(page)
        # print(url)
        res=requests.get(url=url,headers=self.head)
        html=res.content.decode('utf-8')
        return html

    def guolv(self,html):
        patt=re.compile('</div> <div class="col-sm-9">(.*?)<div class="text-center">',re.S)
        itmes=patt.findall(html)
        # print(html)
        patt1=re.compile('<a href="http://www.doutula.(.*?)"',re.S)
        itmes1=patt1.findall(itmes[0])
        # print(itmes1)
        patt2=re.compile('<div class="random_title">(.*?)<div',re.S)
        itmes2=patt2.findall(itmes[0])
        shu=itmes2.count('赞助商广告</div>\n')
        for i in range(shu):
            itmes2.remove('赞助商广告</div>\n')
        print(len(itmes1),len(itmes2))
        mn=list(zip(itmes1,itmes2))
        return mn
    def save(self,mn):
        for i in range(len(mn)):
            os.mkdir(r'C:\Users\LIU\Desktop\地理中国\{}'.format(mn[i][1]))
            zurl='http://www.doutula.'+mn[i][0]
            res=requests.get(url=zurl,headers=self.head)
            zhtml=res.content.decode('utf-8')
            pattg=re.compile("this.src='(.*?)'")
            gurl=pattg.findall(zhtml)
            zts = 1
            for j in gurl:
                # print(j[-3:])
                html=requests.get(url=j,headers=self.head)
                tu=html.content
                # print(j[3:])
                with open(r'C:\Users\LIU\Desktop\地理中国\{}\{}.{}'.format(mn[i][1],zts,j[-3:]),'wb')as f:
                    f.write(tu)
                zts+=1
                print(zts)

            # print('http://www.doutula.'+mn[i][0],mn[i][1])

pa=Doutu()
for i in range(1,8):
    html=pa.qing(i)
    mn=pa.guolv(html)
    pa.save(mn)

# import requests
# import re
# import xlwt
# class Boss():
#     def qing(self,page):
#         url='https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=60&cityId=653&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&_v=0.04493661&x-zp-page-request-id=b9e23123517b42f099d032cb4d9639fe-1542116439816-428578'.format(page)
#         print(url)
#         head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
#         respones=requests.get(url=url,headers=head)
#         html=respones.content.decode('utf-8')
#         return html
#     def guolv(self,html):
#         patt=re.compile('"jobName":"(.*?)"',re.S)
#         gongsi=patt.findall(html)
#         patt1=re.compile('"emplType":"(.*?)"',re.S)
#         shijian=patt1.findall(html)
#         patt2=re.compile('"salary":"(.*?)"',re.S)
#         xinzi=patt2.findall(html)
#         patt3=re.compile('{"code":"103","name":"(.*?)"')
#         jingyan=patt3.findall(html)
#         patt4=re.compile('"eduLevel":{"code":(.*?)}',re.S)
#         xue=patt4.findall(html)
#         patt4_1=re.compile('"name":"(.*?)"',re.S)
#         xueli=[]
#         for i in xue:
#             xuel=patt4_1.findall(i)
#             xueli.append(xuel[0])
#         patt5=re.compile('welfare":(.*?)]',re.S)
#         fuli=[]
#         ful=patt5.findall(html)
#         # print(ful)
#         for j in ful:
#             fuli.append(j.replace('[','').replace('"',''))
#         for q in fuli:
#             print(q)
#         patt5_2=re.compile()
# a=Boss()
# html=a.qing(60)
# a.guolv(html)