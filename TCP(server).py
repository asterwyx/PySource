import socket
import threading
import time
import re
# 服务器是被动连接方，而且大部分时候会同时有很多连接请求，所以服务器编程和普通的有点区别，首先要监听端口，然后再创建特定的socket，这些新建出来的socket交给新线程或者进程处理，实现多线程或者多进程响应
# 创建一个socket绑定一个端口
sListen = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sListen.bind(('127.0.0.1', 9999))
# 启用监听,传入的参数指定等待连接的最大数量
sListen.listen(5)
print("Wait for connection...")

# 处理连接的多线程函数
def tcplink(sock, addr):
    # addr是一个tuple，里面存有客户端的IP地址和端口
    print("Accept new connection from%s:%s..." % addr)
    # 发送欢迎信息
    sock.send(b"Welcome!")
    # 接收客户端发来的数据并进行处理（这里是再字符串的前面加上Hello），因为客户端可能会发来多次请求，所以这里用一个循环来处理
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == re.compile(r"(E|e)xit"):
            break
        sock.send(("Hello," + data.decode('utf-8')).encode('utf-8'))
    sock.close()


# 通过一个永久循环来接受来自客户端的连接，accept()会等待并返回一个客户端的连接
while True:
    # 接受一个新连接
    sock, addr = sListen.accept()
    # 创建新线程处理TCP连接
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()  # 开启新线程