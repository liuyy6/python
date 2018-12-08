#客户端
import socket
#创建socket   封装协议
soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#连接服务器   接受的参数是元组
soc.connect(('192.168.0.37',3000))
aaa='你好'
soc.send(aaa.encode('utf-8'))
#接收响应
msg=soc.recv(1024)
print(msg.decode('utf-8'))

#####################################################################3
# #客户端
# import socket
# #创建socket   封装协议
# soc=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# #发送请求数据
# a=('192.168.0.5',3000)
# aaa='你好呀'
# soc.sendto(aaa.encode('utf-8'),a)
# #接收响应
# c=soc.recv(1024)
# print(c.decode('utf-8'))





