import base64
a = base64.b64encode(b'binary\x00string')
print(a)
b = base64.b64decode(a)
print(b)


# urlsafe编码形式，就是将+和/变成-和_
print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))

print('divider...')

def safe_base64_decode(s):
    while len(s) % 4 > 0:
        s += b'='
    return base64.b64decode(s)

assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')

