import socket
#创建 socket  (封装协议 ：1,ipv4 协议  2,tcp的协议)
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定ip地址和端口号    bind  接受的参数是元组
a=('192.168.0.37',3000)  #192.1.0.0:本机所有ip都可以监听
s.bind(a)
#监听
s.listen(3)  #里面是个任意数字，  数字：最大等待数
while True:
    #接收请求
    a,b=s.accept()   #接收产生两个结果  a:客户端的连接信息  b:存放的客户端的 （ ip地址 ，端口号）
    print(a)
    print('11111111111111')
    print(b)
    #接受数据
    msg=a.recv(1024)  # 512/1024(最大的) : 代表的是每次接受的最大字节数
    print  (msg.decode('utf-8'))
    #发送响应
    reg='welcomewe   you'#  响应信息
    qwe='帅哥，美女才可以哦'
    a.send(reg.encode('utf-8'))
###############################################################################
# import socket
# #创建 socket  (封装协议 ：1,ipv4 协议  2,udp的协议)
# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# #绑定ip地址和端口号    bind  接受的参数是元组
# a=('192.168.0.5',3000)  #192.1.0.0:本机所有ip都可以监听
# s.bind(a)
# while True:
#     #接收请求
#     a,b=s.recvfrom(1024)   #接收数据  a:客户端发送的请求数据  b:存放的客户端的 （ ip地址 ，端口号）
#     print(a.decode('utf-8'))
#     print(b)
#     #发送响应数据
#     msg='welcomewe   you'#  响应信息
#     s.sendto(msg.encode('utf-8'),b)    #前面是发送的数据，后面是发送给谁






