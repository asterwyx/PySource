import hashlib # 提供了常见的字符串摘要算法，比如MD5,SHA1

# 计算一个字符串的MD5值
test = hashlib.md5() # 创建一个md5对象test
test.update('This is written by asterwyx.'.encode('utf-8'))
print(test.hexdigest())

# 数据量很大的时候可以分块多次更新md5对象，每次更新后内容都会变得不一样
test2 = hashlib.md5()
test2.update('first'.encode('utf-8'))
print(test2.hexdigest())
test2.update('second'.encode('utf-8'))
print(test2.hexdigest())