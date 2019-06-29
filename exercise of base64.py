import base64
def safe_base64_decode(s):
    print(type(s))
    l = 4 - len(s) % 4
    if l != 4:
        for i in range(l):
            s += b'='  # 这边得到的s是一个bytes还是一个str？
        print(type(s))
        return base64.b64decode(s)
    else:
        return base64.b64decode(s)

print(type(b'abcd'))
print(b'abcd'.decode('utf-8'))
print('abcd'.encode('utf-8'))
print('divider...')
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('OK')