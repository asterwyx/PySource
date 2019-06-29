import os
print(os.name) # 查看系统的类型，nt表示windows，posix表示linux,unix,Mac os X
print(os.environ)  # 查看设置的环境变量

print("divider......")
print(os.environ.get('PATH')) #用os.environ的get()函数来获取某一个环境变量的值


# 查看当前目录的绝对路径
print(os.path.abspath('.'))
# 在某一目录下创建一个新目录，首先把新目录的完整路径表示出来：
print(os.path.join('d:/asterwyx/Python sources', 'testdir')) # join和split还有splitext函数是用来进行拆分或者组合路径，一般不要用字符串的连接来进行路径的拆分连接，因为linux和windows路径的表示方式并不一样，且并不要求路径真实存在，因为实质上是进行字符串的操作。
# 创建一个新目录
os.mkdir('d:/asterwyx/Python sources/testdir')
# 删除一个目录
os.rmdir('d:/asterwyx/Python sources/testdir')

# 进行文件操作
# 重命名
# os.rename('test.txt', 'test1.py')
# 删除文件
# os.remove('test1.py')
# os模块中并不存在copy函数，但是在shutil模块中是存在一个copyfile()函数来进行文件复制的，shutil模块中还有很多其它对os模块的补充
print([x for x in os.listdir('.') if os.path.isdir(x)])

# 列出所有的python代码(在windows系统中该实现方式无效)
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splittext(x)[1] == '.py'])