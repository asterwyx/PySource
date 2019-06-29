import re
print(re.match(r'\d{3}\-\d{3,8}$','010-12345')) # match()函数用来判断正则表达式是否匹配，如果匹配就i返回一个Match对象，否则返回None

# test = input('请输入要匹配的字符串：')
# if re.match(r'\d{3}\-\d{3,8}$', test):
#     print('OK!')
# else:
#     print('Failed!')

# # 用正则表达式来匹配字符表达：匹配带区号的电话号码
# x = input('请输入一个电话号码：')
# if re.match(r'\d{3}\s+\d{3,5}', x):  # -是特殊字符，不能用\s表示，需要直接用\-转义表示
#     print('OK!')
# else:
#     print('Failed!')

# 要做更精确的匹配，可以用[]表示范围
print(re.match(r'[a-zA-Z0-9\_]', '3'))
print(re.match(r'[a-zA-Z0-9\_]', 't3'))
print(re.match(r'[a-zA-Z0-9\_]+', 'Y6'))
print(re.match(r'[a-zA-Z0-9\_]+', '6_9_T'))


print('divider...')

# 关于行开头标识符^和结束标识符$
print(re.match('^(P|p)ython', 'python'))
print(re.match('^(P|p)ython', 'Python'))
print(re.match('^(P|p)y', 'Python'))
print(re.match('^(P|p)y$', 'Python'))
print(re.match('^(P|p)y$', 'Py'))

# 切分字符串（普通的）
list1 = 'a    b  c'.split(' ')
print(list1)

list1 = 'a    b  c'.split()
print(list1)

# 正则表达式来切分字符串
list2 = re.split(r'\s+','a  b   c')
print(list2)

list3 = re.split(r'[\s+\,]+', 'a  b,   c')
print(list3)

list4 = re.split(r'[\s\,\;]+', 'a  , ; b  c')
print(list4)

# 利用re模块和正则表达式进行字符串分组
# 用()表示的就是要提取的分组

m = re.match(r'(\d{3})(\-)(\d{3,8})', '010-32145')
print(m)
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))
print(m.groups())

# 关于贪婪匹配，Python中默认使用贪婪匹配，会尽量匹配多的字符
n = re.match(r'^(\d+)(0*)$', '103400') # 因为使用贪婪匹配，后面的零不会被分到第二组，而是被归为第一组
print(n.groups())

n = re.match(r'^(\d+?)(0*)$', '103400') # 关闭了贪婪匹配
print(n.groups())

# 预编译提高正则表达式的使用效率
re_telephone = re.compile(r'^(\d{3})\-(\d{3,8})$') # 生成了一个Regular Expression对象
m = re_telephone.match('010-12345698')
print(m.groups())