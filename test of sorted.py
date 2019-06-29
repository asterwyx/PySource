L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(list1):
    list2 = sorted(list1, key = lambda x:(x[0], x[1]))  # 注意sorted函数是以一个列表为参数，复制该列表之后对新的列表对象进行排序，然后审核过程一个新的列表对象，该列表对象会返回，必须要有一个变量接收
    return list2
L = by_name(L)
print(L)

def by_score(list1):
    list2 = sorted(list1, key = lambda x:(x[1], x[0]), reverse = True)
    return list2
L = by_score(L)
print(L)

list3 = [-3, 5, -7, 8, 9, 1]
list4 = sorted(list3)
print(list4)