import smtplib  # 发送邮件的协议
import email.mime.text  # 处理发送的内容
import email.mime.multipart  #  处理邮件的表头

sender = '17839210919@163.com'  #  发送者
recver='1873362204@qq.com'
# recver = ['m15037109541@163.com',
#           '17839210919@163.com',
#           'zhang15660600605@163.com',
#           'xcz201807@163.com']   #  接收者
server = 'smtp.163.com'          #  服务器地址
passwd = 'LYY686789'             #  授权码
# 创建一个空邮件
message = email.mime.multipart.MIMEMultipart()
# 发件人
message['from'] = sender
# 收件人
#message['to'] = recver              #单个人的时候
message['to'] = ','.join(recver)      #只支持字符串
# 主题
message['subject'] = 'python lenrn'
# 正文
text = """
邮件正文写入
hello world,i am 18 岁!!!!
"""
# 处理文本信息
text = email.mime.text.MIMEText(text)
# 将处理后的信息添加到邮件里
message.attach(text)
# ###############################################################################
#                 #附件发送    附件一
#                 att2=email.mime.text.MIMEText(open('py2.py','rb').read(),'base64','utf-8')
#                 att2["Content-Type"]='application/octet-stream'
#                 att2["Content-Disposition"]='attachment;filename="py2.py"'
#                 message.attach(att2)
#                 #附件二
#                 att1=email.mime.text.MIMEText(open('py3.py','rb').read(),'base64','utf-8')
#                 att1["Content-Type"]='application/octet-stream'
#                 att1["Content-Disposition"]='attachment;filename="py3.py"'
#                 message.attach(att1)
#                 #附件三…………
#
# ###############################################################################
# 定义服务器和端口
smtp123 = smtplib.SMTP_SSL(server,465)
# 登录服务器
smtp123.login(sender,passwd)
# 发送邮件
smtp123.sendmail(sender,recver,message.as_string())
# 断开连接
smtp123.close()

##########################################################################################
##########################################################################################
#########################################################################################
#时间模块

# import time
# #
# print(time.time())       #时间戳   代表从公元1970年到现在经过的秒数
# #
# print(time.localtime(813444660.0))     #本地时间     显示的是元组， 默认显示的是当前时间
# # #索引只会显示数值，不会显示字母
# # #括号里可以填时间戳    显示结果为时间戳（时间戳可以增、减）对应的时间
# print(time.strftime('%Y %m %d %H-%M-%S %w',time.localtime()))
# # #显示的结果为        年  月 日 时分秒   星期
#
# print(time.strptime('1970 12 12 6','%Y %m %d %H'))     #将现代化时间转换为元组   “一一对应”
#
#
# b=(1995,10,12,4,50,60,12,121,2)         #自定义时间 ，前六个必须写，后三个随便写
# print(time.mktime(b))                         # 将元祖的时间转化为时间戳
#

# time.sleep(10)        #休眠
# print('1232123')


##################################################3
#判断闰年  ，星期 ，一年中第几天
# a=input('>>>>>>>>>>')
# b=int(a[0:4])
# if b%4==0:
#     print('闰年')
# elif b%400==0:
#     print("闰年")
# else:
#     print('不是闰年')
# aa=('{},{},{},'.format(b,int(a[4:6]),int(a[6::])))
# ww=time.strptime('{} {} {} '.format(b,int(a[4:6]),int(a[6::])),'%Y %m %d ')
# print('今天是周{}'.format(ww[-3]+1))
# print('今天是一年中的{}天'.format(ww[-2]))
# print(time.mktime(ww))
###############################################################
#输入日期（年，月，日）     输出：日期的前一天
# a=input('>>>>>>>>')
# yuanzu=time.strptime('{} {} {}'.format(int(a[:4]),int(a[4:6]),int(a[6:])),"%Y %m %d")
# shijianchuo=(time.mktime(yuanzu)-86400)
# qian=time.localtime(shijianchuo)
# print(time.strftime('%Y %m %d %H-%M-%S %W',qian))
#############################################################################



