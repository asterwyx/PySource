from collections import Iterator
# 用代码展示Iterable(可迭代对象)和Iterator(迭代器)直接的关系
generator = (x * x for x in range(10))
g = generator
print(isinstance(g,Iterator))
print(isinstance([],Iterator))
print(isinstance((),Iterator))

# 使用inter()函数使list和tuple变成Iterator
print(isinstance(iter([]),Iterator))
print(isinstance(iter(()),Iterator))