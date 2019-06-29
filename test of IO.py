# 因为文件读写每一步都可能会出现IOError，一旦出现错误系统就不会执行f.close()，所以用try finally语句来保证f.close()一定会执行
try:
    f = open('D:/asterwyx/Python Sources/test.txt', 'r')
    print(f.read())
finally:
    f.close() # 关闭文件读写以免浪费系统资源
# 用with方法来保证写（读）完即关
with open('D:/asterwyx/Python Sources/test.txt', 'r') as f:
    print(f.read())

# with open('D:/asterwyx/Python Sources/test.txt', 'w') as f:
    # f.write("Hello")

with open('D:/asterwyx/Python Sources/test.txt', 'r') as f:
    print(f.read())

print('divider......')      
with open('D:/asterwyx/Python Sources/test.txt', 'r') as f:
    for l in f.readlines():
        print(l.strip())

print('divider......')
with open('D:/asterwyx/Python Sources/test.txt', 'r') as f:
    print(f.read(2))
    print(f.read(3))

print('divider......')
# with open('D:/asterwyx/Python Sources/test.txt', 'a') as f:
#     f.write('Hello')