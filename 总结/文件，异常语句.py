# f=open(r'C:\Users\LIU\Desktop\aa.txt','a',encoding='utf-8')
# f.write('sfsdfsdfsdf'\n'sdasdasasasdasasdadassda'\n)
# f.close()
# for a in range(1,10):
#     for j in range(1,a+1):
#         a='{}*{}={}'.format(a,j,a*j)
#         print('{}*{}={}'.format(a,j,a*j),end='\t')
#         print()
#
#         for i in range(10):
# f=open(r'C:\Users\LIU\Desktop\aa.txt','w',encoding='utf-8')
# for a in range(1,10):
#     for j in range(1,a+1):
#         f.write('{}*{}={}'.format(a,j,a*j))
#     f.write('\n')
# f.close()

# f=open('a.txt','w')
# f.write('259945276504313283.jpg')
# print(f)

# #f=open(r'C:\Users\LIU\Desktop\259945276504313283.jpg','rb')
# bb=(open(r'C:\Users\LIU\Desktop\259945276504313283.jpg','rb')).read()
# # f.close()
# # print(bb)
# open(r'C:\Users\LIU\Desktop\qqqttttttq.jpg','wb').write(bb)
#
# # print(b)
# # open(r'C:\Users\LIU\Desktop\qqqq.jpg','wb').close()
# with open('a.txt','r',encoding='utf-8') as f:
#     b=f.readlines()
# print(len(b))
# a=0
# for i in b:
#     if i[0]=='#':
#         a+=1
# print(a)
# bb=0
# for j in b:
#     if len(j)==1:
#         bb+=1
# print(bb,len(b)-a-bb)


# with open('bb.txt','r',encoding='utf-8') as f:
#         a=f.readlines()
#         print(len(a))
# for i in a:
#     if i=='\n' or i[0]=='#':                        #i.startswith('#')
#
#         a.remove(i)                #
#     print(len(a))


# for i in range(10):
#     with open('{}.txt'.format(i),'w',encoding='utf-8') as ai:
#         for j in range(10):
#             ai.write('wewrwerwrwer''\n')
# import os
# for i in range(10):
#     # with open(r'C:\Users\LIU\Desktop\259945276504313283.jpg','rb') as ai:
#     #     aii=ai.read()
#     #     with open('a{}.jpg'.format(i),'wb') as aai:
#     #         aai.write(aii)
#     os.remove('a{}.jpg'.format(i))

# a=input('>>>>>>>>>>')
# try:
#     a+=1
# except TypeError and NameError as x:
#     print(x)
#     print('holle')


# try:
#     a=1
#     b=a+1
#     print(b)
# except TypeError as x:
#     print(x)
#     print('holle')
# else:
#     print('hi')
# finally:
#     print('ssssssssssss')


##################################################
                                                    #触发异常
# a=123
# raise Exception('报错了吧')
########################################################################################3
#import chaoshi

# from chaoshi import sgwc
# sgwc()




# a=input('>>>>>>>')
# try:
#     a='AAS'+1
# except TypeError as x:
#     print(x)
#     print('bbbbbbbbbbbbbbbbbbbbbbbbb')
# else:
#     c=a+1
#     print(c)
# finally:
#     aa=99
#     print(aa)
# #raise NameError('baocuoleba'):
#     #print('999999999999999999999')
# a=input('》》》》》》》》》》》')
# try:
#     a=int(a)
# except Exception as x:
#     print('ssssssssssssssssssssssss')
# else:
#     print('aaaaaaaaaaaaaaaaaaa')
# finally:
#     print('ppppppppppppppppppppp')
# raise NameError('报错了吧')
# # print('ccccccccccccc')
# # print('hhhhhhhhhhhhhhhhhhhhh')

import os
os.rename('py3.py','文件，异常语句.py')



