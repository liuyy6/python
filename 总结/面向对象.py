#/usr/bin/evn python
# --*--coding:utf-8 -*-
# class Shuzi():     #为了跟函数名区分，类名首字母一般为大写
#     def jiujiu(self):       #必须加上 self
#         print('jiujiuchengfa')
#     def paixu(self,a):    #传参，a
#         print('sfdsfdsdfdsf')
# a=shuzi()     #类的实例化
# a.paixu(3)    #调用类里面的函数(fangfa)
# shuzi().jiujiu()
# a.jiujiu()
# b='weqw'
# print(type(b))


# #Eg:
# class shili():
#     def jiujiu(self,a):
#         b=1
#         d=0
#         for i in range(1,a+1):
#             b*=i
#             d+=b
#         return d
#     def zhishu(self,x):
#         a=self.jiujiu(x)
#         c = 0
#         for i in range(2,a+1):
#             for j in range(2,i):
#                 if i%j==0:
#                     break
#             else:
#                 c+=i
#         print(c)
# # shili().zhishu(5)
#
#
#
#
# class shu():
#     def aa(self):
#         print('dsffsfsdf')
# class zi():
#     def asd(self,s):
#         print('sdfsdfds')
#     def aa(self):
#         print('qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq')
# class qq(shu,zi):
#     pass
# # a=qq()
# # # a.aa()
# # a.asd(4)
# # c=zi()
# # c.aa()
# # class shuzi2(shili):
# #     pass
# # asd=shuzi2()
# # print(asd.jiujiu(6))




# #多态
# class shuzi():
#     def aa(self):
#         print("sdsdasdasas")
# class zhishu():
#     def bb(self):
#         print('qqqqqqqqqqqqqqq')
# class jiecheng():
#     def __cc(self):
#         print('wwwwwwwwwwwwwwwwwwww')
# class aaa(shuzi,zhishu,jiecheng):
#     def aa(self):     #方法重写，在这个类中调用的aa是最新的，更新后的aa
#         print('aaaaaaaaaaaaaaaaaaaaaaaaaa')
# class cc(shuzi,zhishu):
#     def dd(self):
#         print('ccccccccccc')
# class dd():
#     a='11111111111111111111111111'
#     def __init__(self,a,b):       #调用dd这个类里面的方法，运行的第一个程序，
#         self.a=a         #更新属性，作用于全类
#         self.b=b
#     def ass(self,c):
#         print(self.b,c)      #self.b调用这个类的属性b（类的传参），c是方法的传参
# az=dd(12,35678904)    #必须参数的传参
# az.ass(2)             #函数的传参




# class shuzi():
#     def zhishu(self,a,b):
#         bb=0
#         for i in range(a,b):
#             for j in range(2,i):
#                 if i%j==0:
#                     break
#             else:
#                 bb+=i
#         print(bb)
#     def huiwen(self,a):
#         b=a[::-1]
#         if a==b:
#             print('是回文')
#         else:
#             print('不是回文')
# a=shuzi()
# a.zhishu(2,100)
# a.huiwen('qwertyuuytrewq')
# a.huiwen('fdhgkjjhgh')

# a=4*-3
# a=int(a)
# print(type(a))
############################################################################################
#/usr/bin/env python
#-*- coding:utf-8 -*-
# class Gouwuche():
#     def gouwuche(a):
#         zongjia=0
#         while True:
#             a=input('请输入你要购买的物品，退出:exit：')
#             if a=='exit':
#                 break
#             else:
#                a+=self.b[int(a)]
#
#
# a=int(input('请输入总资产：'))
# b=[1999,10,20,998]
# c=['电脑','鼠标','游艇','美女']
# for i in range(4):
#     ai={}
#     ai['name']=c[i]
#     ai['price']=b[i]
#     print(1+i,ai)


import os
os.remove('leideyingyong.py')
