import socket


# 创建socket实例
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 获取本机电脑名
myname = socket.getfqdn(socket.gethostname())
print("打印电脑名：" + myname)
# 获取本机ip
myaddr = socket.gethostbyname(myname)
print("打印IP：" + myaddr)
# 绑定IP和端口
server.bind((myaddr, int(4099)))
# 开始监听
server.listen(5)
print("监听中......")
# 连接
conn, addr = server.accept()
print("连接方IP：%s" % (str(addr)))
client_msg = conn.recv(1024)
print("密码：%s" % (str(client_msg)))
conn.send(client_msg.upper())
conn.close()
server.close()