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
# chain()函数把多个迭代对象连接成一个更大的迭代对象
for c in itertools.chain("ABC", "XYZ"):
    print(c)
# groupby()用于把迭代对象中相同的元素挑出来放在一起，相同的元素有一个相同的key
for key, group in  itertools.groupby("AAAABBCCCDDD"):
    print(key, list(group))
# 事实上groupby()函数是通过某一个函数的返回值来分类的，迭代对象中的每一个元素是传入其中的参数，如果返回值相同，就会被归为一组，返回值作为分组的key，可以自定义groupby()函数的第二个参数来传入一个匿名函数
for key, group in itertools.groupby("AAaBbbBDDDdDCCccCc", lambda c: c.upper()):
    print(key, list(group))


def judge(c):
    if c.upper() == c:
        return 1
    else:
        return 0

for key, group in itertools.groupby("AAaBbbBDDDdDCCccCc", judge):
    print(key, list(group))
# 从这个例子可以看出，groupby()函数只能把相邻的key相同的元素分为一组，对于中间隔了一个key不相同的某两个key相同的元素，也是不能分为一组的（因为不能够更改可迭代对象的顺序）


