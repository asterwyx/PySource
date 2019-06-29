# from collections import Iterable
# 迭代list,tuple等有下标的数据类型
list1 = [6,8,9,5,2,4,8,3,2]
tuple1 = (6,8,9,5,2,4,8,3,2)
for x in list1:
    print(x)
for x in tuple1:
    print(x)

# 迭代一些抽象无顺序的数据类型
dict1 = {'mary':100,'Michael':99,'Cecil':96,'Carolina':93}
for key in dict1:
    print(key)
for value in dict1.values():
    print(value)
for key,value in dict1.items():
    print(key,value)

# 实现Java一样的下标循环
for x,y in enumerate(list1):
    print(x,y)

# 判断一个数据是否可迭代
# print(isinstance( 'ABC', Iterable))
# print(isinstance({'mary':100,'Michael':99,'Cecil':96,'Carolina':93}, Iterable))
# print(isinstance([1,2,3], Iterable))
# print(isinstance(123, Iterable))

# 使用迭代求出一个list中的最大最小值

# 定义函数
def findmaxmin(L):
    if L == []:
        return
    else:
        min = L[0]
        max = L[0]
        for x in L:
            if x >= max:
                max = x
            if x <= min:
                min = x
        return min, max
    

# 调用函数以及检验正误
x, y=findmaxmin([])
print(x,y)
if (x, y) != (2,9):
    print('测试失败！')