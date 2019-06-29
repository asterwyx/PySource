def slice_space(s):
    if s[0] == ' ':
        s = s[1:]
    if s[-1] == ' ':
        s = s[:-1]
    return s
# string = input('Please enter a string')
string1 = ' hello world '
string2 = 'hello world '
string3 = ' hello world'
string4 = 'hello world'
sliced_string1 = slice_space(string1)
sliced_string2 = slice_space(string2)
sliced_string3 = slice_space(string3)
sliced_string4 = slice_space(string4)
if sliced_string1 != 'hello world':
    print('测试失败！')
elif sliced_string2 != 'hello world':
    print('测试失败！')
elif sliced_string3 != 'hello world':
    print('测试失败！')
elif sliced_string4 != 'hello world':
    print('测试失败！')
else:
    print('测试成功！')