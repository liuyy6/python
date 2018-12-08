#导入正则表达式的模块     re ：只能匹配（过滤）字符串
import re
# a='qwe123qweqwe456qwe'
# #首先将要匹配的正则编译
# b=re.compile('qwe(.{3})qwe')  #查找   括号里的
# bb=re.compile('qwe')    #查找   qwe
# bbb=re.compile('qwe(.*)qwe')
# #到目的字符串中去查找
# c=b.findall(a)
# cc=bb.findall(a)
# ccc=bbb.findall(a)
# print(c)
# print(cc)
# print(ccc)
########################################
                    #贪婪模式:尽可能多的去匹配最后的字符串
                    #非贪婪模式：尽可能少的匹配最后的字符
                    #带有  ？ 的是非贪婪模式（优先级高），带有  *  贪婪模式
# z='qwe123qweqwe456qwe'
# y=re.compile('qwe(.*)qwe')
# yy=re.compile('qwe(.*?)qwe')
# h=y.findall(z)
# hh=yy.findall(z)
# print(h)    #贪婪
# print(hh)   #非贪婪
#################################################
#    .可以匹配任意一个字符，但是不能匹配换行符
#解决办法     加入  re.s    产生的结果是列表
p="""qwe12
3qweqwe456Qwe"""
o=re.compile('qwe(.*?)qwe',re.S)
oo=re.compile('qwe(.*)qwe',re.I)      #  re.I:匹配的字符不区分大小写
i=o.findall(p)
ii=oo.findall(p)
print(i)
print(ii)

