import threading
import socket
# 还是要创建一个socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # DGRAM指明该socket使用的是udp协议
# 绑定端口，但是不需要监听不需要接受连接就可以直接接收数据包
s.bind(('127.0.0.1', 9999))


def udplink(data, addr):
    print("Received data from %s:%s" % addr)
    ns = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ns.sendto(b"Hello, %s" % data, addr)
    ns.close()

while True:
    data, addr = s.recvfrom(1024)  # recvfrom()函数直接返回数据和地址
    t = threading.Thread(target=udplink, args=(data, addr))
    t.start()
