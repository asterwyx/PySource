import socket
# 创建一个socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接
s.connect(("www.sina.com.cn", 80))
# 建立了连接之后就可以发送数据了
s.send(b'GET / HTTP /1.1\r\nHost:www.sina.com.cn\r\nConnection:close\r\n\r\n')
# 接收数据
buffer = []
while True:
    # 每次最多接收1k字节
    d = s.recv(1024)  # 调用recv(max)方法接收数据,max是最多接收字节数
    # 处理数据，如果接收的数据不是空的，就写入缓存
    if d:
        buffer.append(d)
    else:
        break
# 将接收到的数据连接起来
data = b''.join(buffer)
# 接受完数据后，调用close()方法关闭socket
s.close()

# 处理数据
# 先把http头和主体分开
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
with open('sina.html', 'wb') as f:
    f.write(html) 