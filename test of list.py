classmates = ['Michael','Bob','Tracy']
number = range(5)
number = list(number)
print(number)
sum = 0
for x in number:
    sum = sum + x
print(sum)
for classmate in classmates:
    print(classmate)
# name = input('Please enter your name:')
# classmates.append(name)
# print(classmates)
# classmates.insert(0,name)
# print(classmates)
# classmates.pop(2)
# print(classmates)
# print(len(classmates))



# 高级特性中的list生成式
list1 = list(range(1,11))
print(list1)

# 此种方法并不能生成想要的数据
list2 = [range(1,11)] # 此种表示是错误的
for x in list2:
    print(x)
print(list2)
# 稍做一些修改
list2 = [x for x in range(1,11)] # 此行被称为列表生成式
for x in list2:
    print(x)
print(list2)
# 生成整数的平方的列表
list3 = [x**2 for x in range(1,11)]
print(list3)

# 生成偶数的平方
list4 = [x**2 for x in range(1,11) if x % 2 == 0]
print(list4)

# 两层循环，构成全排列
list5 = [x + y for x in 'ABC' for y in 'XYZ']
print(list5)
# for循环同时使用两个或多个变量（与多层for循环有差别）
dict1 = {'Mary':'100','Michael':'99','Cecil':'96'}
list6 = [k + '=' + v for k, v in dict1.items()]
print(list6)

# 构造一个列表生成式，选取已知list中的字母字符串并使其以小写的形式表示
list0 = ['Hello','WorLd','IBM',123,True,]
list7 = [s.lower() for s in list0 if isinstance(s,str)]
print(list7)

def test_list(L):
    L = [0]
    return

list8 = [9, 7, 8, 6, 5]
test_list(list8)
print(list8)

def test_list1(L):
    L[0] = 0
    return

list8 = [9, 7, 8, 6, 5]
test_list1(list8)
print(list8)