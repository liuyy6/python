# /usr/bin/evn python
# --*--coding:utf-8 -*-
import random


# a=random.randrange(1,10)
# print(a)
############################################
# 法一                     九九乘法表
# for i in range(1,10):
#     for a in range(1,i+1):
#         b='{}*{}='.format(i,a)
#         # c=b.format(i,a)
#         print(b,i*a,end='\t')
#     print()
# # 法二                                                                 九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{}*{}={}'.format(j,i,i*j),end='\t')
#     print()
# #  a=[1,21,1,32321]
# # for i in a:
# #     if i%2==0:
# #         break
# # else:
# #     print('无偶数')
# import random                             #游戏判断
# a=random.randrange(1,10)
# for i in range(3):
#     print('还有{}次'.format(3 - i))
#     b=int(input('请输入：'))
#     if b>a:
#         print('大了')
#     elif b<a:
#         print('小了')
#     elif b==a:
#         print('优秀')
#         break
# else:
#     print('笨蛋')
# # a=0
# # for i in range(2,100):
# #     for j in range(2,i+1):
# #         if i%j==0:
# #             break
# #     if i==j:
# #         a+=i
# #
# # print(a)
# # for i in range(100,999):                                # 水仙花束
# #    a=i//100
# #    b=i//10%10
# #    c=i%10
# #    if a**3+b**3+c**3==i:
# #        print(i)


# # e=input('请输入：')                              #阶乘之和
# # a=int(e)
# # c=0
# # for i in range(1,a+1):
# #     b=1
# #     for j in range(1,i+1):
# #         b*=j
# #     c+=b
# # print(c)

# # #法一
# # a=input('请输入：')                           #去重排序(排序按照的是acces表)
# # a=a.split(',')
# # for i in a:
# #     if a.count(i)>2:
# #         for b in range(a.count(i)-1):
# #            a.remove(i)
# # a.sort()
# # print(a)
# # 法二
# # a=input('请输入：')                           #去重排序
# # a=a.split(',')
# # b=[]
# # for i in a:
# #     if i not in b:
# #         b.append(i)
# # b.sort()
# # print(b)
#
# # a=input('请输入：')
# # a=a.split(',')
# # for i in range(len(a)):
# #     for j in range(len(a)):
# #         if int(a[j])>int(a[j+1]):
# #             b=a[j]
# #             a[j]=a[j+1]
# #             a[j+1]=b
# # int(a[i])
# # print(a)
#
# # a=1
# # while 0<a<10:
# #     print(a,end=(''),\'t')
# #     a+=1

# a=1                                               #0到100 相加
# b=0
# while a<101:
#     b+=a
#     a+=1
# print(b)
# # import random
# # a=random.randrange(0,100)
# # while True:                    #猜数字的游戏
# #  b=input('请输入：')
# #  b=int(b)
# #  if b>a:
# #         print('数字大了')
# #  elif b<a:
# #         print('数字小了')
# #  elif b==a:
# #     print('优秀的人啊')
# #     break
#
# # a=1
# # while a<10:
# #     b=1
# #     while b<a+1:
# #         print('{}*{}={}'.format(a,b,a*b),end='\t')
# #         b+=1
# #     print()
# #     a+=1
#
# # a=0
# # for i in range(2,100):
# #     for j in range(2,i):
# #         if i%j==0:
# #             break
# #     else:
# #         a+=i
# # print(a)
#
#########################################################
#手动输入一组数，打印平均数以下的数，一直输到输入exit退出
# c=[]
# while True:
#     c.clear()
#     a = input('请输入：')
#     if a=='exit':
#         break
#     else:
#         a = a.split(',')
#         for i in a:
#             b=int(i)
#             c.append(b)
#             d=sum(c)/len(c)
#         print(d)
#         for j in c:
#             if j < d:
#                 print(j)

# # 思路
# # # b=['12','12','3','2244','23']
# # # for i,j in enumerate(b):
# # #     b[i]=int(j)
# # # print(b)
#
#
# # b=1
# # b='qwqe'
# # print(b)




# # a=input('>>>>>>>')                             #判断字符串是否是回文
# # b=0
# # for i in a:
# #     b-=1
# #     if i!=a[b]:
# #         print('不是回文')
# #         break
# # else:
# #     print(a)
# a=[12,342,342,344,24,213,42421,312312,23]
# for i in range(len(a)):
#     for j in range(len(a)-1-i):
#         if a[j] > a[j+1]:
#             c=a[j+1]
#             a[j+1]=a[j]
#             a[j]=c
# print(a)

# c=[]                                         #冒泡排序法
# a=input('请输入：')
# a=a.split(',')
# for i in a:
#     c.append(int(i))
# b=len(c)
# f=0
# while f<b:
#     for j in range(b-1):
#         if c[j]>c[j+1]:
#             e=c[j]
#             c[j]=c[j+1]
#             c[j+1]=e
#     f+=1
# print(c)
# t=[]
# a=input('>>>>')
# a=a.split(',')
# b=len(a)
# for q in a:
#     t.append(int(q))
# t=[]
# a=input('>>>>>>>>')
# a=a.split(',')
# b=len(a)
# for q in a:
#     t.append(int(q))
# for i in range(b):
#     for j in range(b):
#         if t[i]>t[j]:
#             e=t[i]
#             t[i]=t[j]
#             t[j]=e
# print(t)
# # a=3998
# # for i in a:
# #     a=a%16
# #     b=3998//16
# #     print(a,b)
#
# # a=input("请输入")                        #进制转换十进制转二进制
# # a=int(a)
# # q=[]
# # w=[]
# # while True:
# #     for i in range(a,a+1):
# #         a=i//16
# #         b=i%16
# #         q.append(b)
# #     if a==0:
# #         break          #跳出循环  while True
# # for a in q:
# #     if a==10:
# #         w.append('A')
# #     elif a==11:
# #         w.append('B')
# #     elif a==12:
# #         w.append('C')
# #     elif a==13:
# #         w.append('D')
# #     elif a==14:
# #         w.append('E')
# #     elif a==15:
# #         w.append('F')
# #     else:
# #         w.append(a)
# # w.reverse()
# # for p in w:
# #     print(p,end='')
#
#
# # a=int(input('请输入数'))
# # c=[]
# # while True:
# #     if a>0:
# #         b=a%16
# #         a//=16
# #         c.append(b)
# #     elif a==0:
# #         break
# # c.reverse()
# # print(c)
#
#
# # a=input('>>>>>>>>>')
# # a=a.split(',')
# # o=[]
# # c=[]
# # for p in a:
# #     q=int(p)
# #     o.append(q)
# #     c=o.copy()
# # for i in range(len(a)):
# #     for j in range(len(a)-1):
# #         if o[j]>o[j+1]:
# #             e=o[j]
# #             o[j]=o[j+1]
# #             o[j+1]=e
# # print(o,c)         #可写可不写
# # print(o[-1],o[-2])
# #
# # a=input('>>>>>>>>>>')                 字符串转换成数字，不用int
# # b=a[::-1]
# # h=0
# # for i,j in enumerate(b):
# #     for n in range(10):
# #         if str(n)==j:
# #             h+=n*10**i
# # print(h)
#                                                # 十进制转十六进制
# # a=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
# # b=input('>>>>>>>>>>')
# # c=int(b)
# # f=''
# # while True:
# #     d = c % 16
# #     c=c//16
# #     f+=a[d]
# #     if c==0:
# #         break
# # print(f[::-1])
#                                             # 十进制转十六进制
# # a=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
# # b=int(input('请输入'))
# # f=''
# # while True:
# #     c=b%16
# #     b=b//16
# #     f+=a[c]
# #     if b==0:
# #         break
# # print(f[::-1])
#
# # a=[23,543,3423,0,3434]                            #最大最小换位置
# # c=a.copy()
# # c.sort()
# # e=a.index(c[0])
# # n=a.index(c[-1])
# # a[n],a[0]=a[0],a[n]
# # a[e],a[-1]=a[-1],a[e]
# # print(a)
#
#
# # /usr/bin/env python
# # --*--coding：utf-8  -*-
# # a=input('>>>>>>>')
# # a=a.split(',')
# # b=[]
# # qc=set()
# # for i in a:
# #     intt=int(i)
# #     b.append(intt)
# # for q in range(len(b)):
# #     for j in range(len(b)-1):
# #         b[j],b[j+1]=b[j+1],b[j]
# #         w=tuple(b)
# #         qc.add(w)
# # for qcf in qc:
# #     for z in qcf:
# #         zf=int(z)
# #         print(zf,end='')
# #     print()
#
#
#
#
#
#
#
# #                                     四个数字，组合成三位数，不重复
# # a=input('>>>>>>>')
# # a=a.split(',')
# # b=[]
# # qc=set()
# # for i in a:
# #     intt=int(i)
# #     b.append(intt)      #字符串转化为数字
# # for b1 in range(4):
# #     b11=b[b1]           #提取将要删除的元素
# #     b.pop(b1)
# #     for q in range(len(b)):
# #         for j in range(len(b)-1):
# #             b[j],b[j+1]=b[j+1],b[j]    #排列组合
# #             w=tuple(b)                  #转化成元组
# #             qc.add(w)                  #加入到集合，去重
# #     b.insert(b1,b11)                 #上面删掉一个元素，补充进元素
# # for qcf in qc:                      #在集合中提取元素，组合成的数字（元组形式）
# #     for z in qcf:
# #         zf=int(z)
# #         print(zf,end='')          #将元组中中数据提取出来，元组转化成数字
# #     print()
# # print(len(qc))
#
#
# # aa=input('>>>>>>')                       # 四个数任意三个组成一组数
# # qc=''
# # qc1=set()
# # for i in range(4):
# #     for a in range(4):
# #         if a!=i:
# #             for b in range(4):
# #                 if b!=i:
# #                     if b!=a:
# #                         qc='%s%s%s'%((aa[i]),(aa[a]),(aa[b]))
# #                         qc1.add(int(qc))
# # for jg in qc1:
# #     print(jg)
# # print(len(qc1))
#
# # a=123
# # def sss():
# #     global a
# #     a='qqqqqqqqqq'
# #     #print(a)
# #     return a
# # sss()
# # print(a)
#
# # a=input('>>>>>')
# # a=a.split(',')
# # for i in range(len(a)-1):
# #     a[i],a[i+1]=a[i+1],a[i]
# # print(a)
#
#
# # def su(x):
# #     a=0
# #     for i in range(2,x):
# #         for j in range(2,i+1):
# #             if i%j==0:
# #                 break
# #         if i==j:
# #             a+=i
# #     print(a)
# # su(100)
#
# #
# # for i in range(2,100):                      #因数之和
# #     a = 0
# #     for j in range(1,i):
# #         if i%j==0:
# #             a+=j
# #     if a==i:
# #         print(a)
# def ss():
#     print('你是最棒的')
#
# if __name__=='__main__':
#     print('加油！')
#     return
