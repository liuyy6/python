import os
# a=os.popen('control')    #打开计算机命令
# print(a.read())           #读取
# print(os.getcwd())
# # os.chdir(r'C:\Users\LIU\Desktop')
# # print(os.getcwd())
# # os.mkdir('lyy')
# os.makedirs(r'aaa\bbb\ccc')
#os.remove('a2.txt')
# os.removedirs(r'aaa\bbb\ccc')
# print(os.listdir(r"C:\Users\LIU\Desktop"))
os.rename('面向对象','面向对象.py')
# print(os.path.splitext(r'C:/Users/LIU/Desktop/python/模块.py'))
# print(os.path.isfile('a.txt'))
# # print(os.path.isdir('liu'))
# # print(os.path.islink('a8.txt'))
# # print(os.listdir())



# a=os.listdir()
# aa=0
# b=0
# c=0
# for i in a:
#     if os.path.isfile(i):
#         print('普通文件')
#         aa+=1
#     elif os.path.isdir(i):
#         print('目录')
#         b+=1
#     elif os.path.islink(i):
#         print('连接文件')
#         c+=1
#     else:
#         print('其他文件')
# print('普通文件{}'.format(aa),'目录文件{}个'.format(b),'连接文件{}'.format(c))
# a=[i for i in os.listdir() if os.path.isfile(i)]
 # b=[y for y in os.listdir() if os.path.isdir(y)]
# print(len(a),len(b))