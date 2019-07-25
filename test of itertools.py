import itertools
# 创造一个无限迭代器
iteral = itertools.count(start=1 ,step=2) # 创造一个从1开始，步长为2的一个无限迭代器
for i in range(20):
    print(next(iteral))
# cycle()用来无限重复传入的一个序列(可迭代对象)
cs = itertools.cycle("ABC")
for i in range(20):
    print(next(cs))
# repeat()函数用来重复某一个迭代元素，可以设置迭代次数
repeatition = itertools.repeat("ABC", 6)
for r in repeatition:
    print(r)