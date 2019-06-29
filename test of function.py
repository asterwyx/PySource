# 导入函数库
import math
from my_function import my_abs
from my_function import my_square
from my_function import quadratic #测试一次返回多个函数值

# 尝试是否可以用list或set或dict作为max函数的参数
L = [1,5,5,85,4,5,6,2,3,9,7,2,8]
maximum = max(L)
print(maximum)

S = set(L)
maximum = max(S)
# 测试是否存在min函数
minumum = min(S)
print(maximum)
print(minumum)

# 特别测试是否可以用dict作为参数
D = {'Mary':100,'Michael':99,'Cecil':93,'Adam':96}
maximum = max(D)
print(maximum)

# 测试绝对值函数
x = 2
jueduizhi = abs(x)
print(jueduizhi)

# 测试数据类型转换函数
x = int('123')
print(x)
y = str(12.35)
z = float('12.35')
print(y,'\n',z)

# 测试bool类型转换
test1 = bool(1)
test2 = bool(0)
test3 = bool('')
test4 = bool(',')
test5 = bool('\n')
print(test1)
print(test2)
print(test3)
print(test4)
print(test5)

# 测试将一个整数转换成16进制表示的字符串
n1 = 255
n2 = 1000
hn1 = hex(n1)
hn2 = hex(n2)
print(hn1)
print(hn2)

# 测试从自己写的文件中导入的函数，体验多文件程序
print(my_abs(-2))
print(my_square(4))

# 测试函数参数数据类型检验函数isinstance()
# def myabs(x):
#     if not isinstance(x,(int,float)):
#         raise TypeError('bad operand type')
#     if x > 0:
#         return x
#     else:
#         return -x
# print(myabs('A'))

# 用自定义的函数测试一次返回多个函数值(返回的是一个tuple)
x1,x2 = quadratic(1,2,-3)
print(x1,x2)

# 测试默认参数
def power(x,n = 2):
    m = 1
    while n > 0:
        m *= x
        n -= 1
    return m
test6 = power(2)
test7 = power(2,3)
test8 = power(1.5,3.5)
print(test6,test7,test8)

# 测试多个默认参数
# def print_person_information(name,gender,age = 18,city = '北京'):
#     print('name:',name,'gender:',gender,'age:',age,'city:',city)
# name = input('Please enter your name:')
# gender = input('Please enter your gender:')
# print_person_information(name,gender)
# print_person_information('Cecil','男',19,'武汉')
# print_person_information('Cecil','男',19)
# print_person_information('Cecil','男',city = '武汉')

# 测试可变参数以及list,tuple,dict作为参数的情况

# 以list作为函数参数
information = ['王溢学','男',19,'武汉']
def print_person_information_update(information):
    for aspect in information:
        print(aspect)
print_person_information_update(information)
print_person_information_update(('王溢学','男','19','武汉'))
print_person_information_update(['王溢学','男',19,'武汉'])

# 一个接收可变参数的函数
def print_person_information_update2(*information):
    for aspect in information:
        print(aspect)
print_person_information_update2(*information)
print_person_information_update2('王溢学','男','19','武汉')