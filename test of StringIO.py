from io import StringIO #  StringIO只能操作str类型数据
f = StringIO()
f.write("Hello, world!")
print(f.getvalue())
f.write('Cecil')
print(f.getvalue())
g = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = g.readline()
    if s ==  '':
        break
    print(s.strip())
# 要实现在内存中读写二进制数据，就必须使用BytesIO
from io import BytesIO
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())