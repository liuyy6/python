import requests  #第三方库，需要下载
#爬虫：又叫 网络蜘蛛（spider）
#模仿浏览器，根据自己制定的规则批量下载
#正则表达式，是用来匹配文件中内容

#模仿浏览器的模块：urllib   urllib2  requests
#匹配内容的模块：re（正则表达式），bs4，xpath
#爬虫分类：1，聚焦爬虫 （只爬取某个网站的资源） 2，搜索爬虫（爬取整个网络中的资源）

#第一步：分析网址的变化
#第二部分析html文件，过滤并下载想要的资源
#第三步保存，保存的  ***权限  ***格式
################################################################
#面向对象代码
#第一步：分析网址的变化
# 'https://www.qiushibaike.com/text/page/{}/'.format(1)
import requests   #所有模块写在最上
import re
class Qiuchong(object):
    def qingqiu(self,page):     #传入参数
        url='https://www.qiushibaike.com/text/page/{}/'.format(page)  #page:页
        #发送请求
        response=requests.get(url=url)   #response：变量名(响应，回答)
        #读取结果的方式： 1.以字符串的方式读取
        #print(response.text)
        #                 2，以字节码的方式读取  ,需要解码
        html=response.content.decode('utf-8') #解码方式是根据源文件中的编码方式   显示的结果为html文件
        return html
    def guolv(self,abc):
        shuju=[]
        patt=re.compile('<div class="content">(.*?)</div>',re.S)    #  列表的形式显示
        items=patt.findall(abc)   #到目的文件中查找
        for i in items:
            i=i.replace('<span>','').replace('</span>','').replace('<br/>','\n')
            i=i.replace('<span class="contentForAll">查看全文','')
            i=i.strip()
            shuju.append(i+'\n')
        return (shuju)
    def save(self,shuju):
        with open('aa.txt','a',encoding='utf-8') as f:
            for i in shuju:
                f.write(i+'\n')

qiu=Qiuchong()
# jieguo=qiu.qingqiu(1)
# shuju=qiu.guolv(jieguo)
# qiu.save(shuju)

for i in range(5):
    jieguo = qiu.qingqiu(i)
    shuju = qiu.guolv(jieguo)
    qiu.save(shuju)

###########$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#爬图片
# import requests
# import re
# url='http://www.doutula.com/article/list/?page=10'
# head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36' }
#        #      User-Agent  :是个固定值      反爬机制
# response=requests.get(url=url,headers=head)
# html=response.content.decode('utf-8')
# patt=re.compile(r'http://www.doutula.com/article/detail/[0-9]{7}')
# itmes=patt.findall(html)
# ################################################
# #爬去每个主题
# a=1000
# for i in itmes:
#     repons=requests.get(url=i, headers=head)
#     html1 = repons.content.decode('utf-8')
#     patt1=re.compile(r'<img src="(.*?)" alt=')
#     itmes1=patt1.findall(html1)
#     # print(itmes1)
#     # print(len(itmes1))
#     for b,j in enumerate(itmes1):
#         print(j)
#         repons2=requests.get(url=j,headers=head)
#         html2=repons2.content
#         if j[-3:]=='jpg':
#             with open('{}.jpg'.format(a),'wb') as ff:
#                 ff.write(html2)
#         # elif j[-3:]=='gif':
#         else:
#             with open('{}.gif'.format(a),'wb') as ff:
#                 ff.write(html2)
#         a+=1
#     print(a)
##########$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#反爬：组织爬虫程序批量下载资源
"""常见反爬手段：  
1.header  信息  
user-Agent:  windows 信息    浏览器版本信息     f13
2.验证码

"""
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$44

#斗图
# import requests
# import re
# import os
# class Doutu():
#     head = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
#     def qing(self,page):
#         url='http://www.doutula.com/article/list/?page={}'.format(page)
#         # print(url)
#         res=requests.get(url=url,headers=self.head)
#         html=res.content.decode('utf-8')
#         return html
#
#     def guolv(self,html):
#         patt=re.compile('</div> <div class="col-sm-9">(.*?)<div class="text-center">',re.S)
#         itmes=patt.findall(html)
#         # print(html)
#         patt1=re.compile('<a href="http://www.doutula.(.*?)"',re.S)
#         itmes1=patt1.findall(itmes[0])
#         # print(itmes1)
#         patt2=re.compile('<div class="random_title">(.*?)<div',re.S)
#         itmes2=patt2.findall(itmes[0])
#         shu=itmes2.count('赞助商广告</div>\n')
#         for i in range(shu):
#             itmes2.remove('赞助商广告</div>\n')
#         print(len(itmes1),len(itmes2))
#         mn=list(zip(itmes1,itmes2))
#         return mn
#     def save(self,mn):
#         for i in range(len(mn)):
#             os.mkdir(r'C:\Users\LIU\Desktop\地理中国\{}'.format(mn[i][1]))
#             zurl='http://www.doutula.'+mn[i][0]
#             res=requests.get(url=zurl,headers=self.head)
#             zhtml=res.content.decode('utf-8')
#             pattg=re.compile("this.src='(.*?)'")
#             gurl=pattg.findall(zhtml)
#             zts = 1
#             for j in gurl:
#                 # print(j[-3:])
#                 html=requests.get(url=j,headers=self.head)
#                 tu=html.content
#                 # print(j[3:])
#                 with open(r'C:\Users\LIU\Desktop\地理中国\{}\{}.{}'.format(mn[i][1],zts,j[-3:]),'wb')as f:
#                     f.write(tu)
#                 zts+=1
#                 print(zts)
#
#             # print('http://www.doutula.'+mn[i][0],mn[i][1])
#
# pa=Doutu()
# for i in range(1,8):
#     html=pa.qing(i)
#     mn=pa.guolv(html)
#     pa.save(mn)

