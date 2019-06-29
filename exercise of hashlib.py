import hashlib
# -*- coding:utf-8 -*-
users = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

def login(username, password):
    password_md5 = hashlib.md5()
    password_md5.update(password.encode('utf-8'))
    if password_md5.hexdigest() == users[username]:
        print('log in successfully!')
        return 1
    else:
        print('password error')
        return 0

assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')