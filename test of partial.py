import functools
int2 = functools.partial(int, base = 2)
number = input('请输入一个二进制数：')
print(int2(number))