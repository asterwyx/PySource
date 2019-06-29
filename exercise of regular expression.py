# 版本一：验证Email的函数
import re
def is_valid_email(addr):
    re_email = re.compile(r'^[a-zA-Z0-9\.]+\@[a-zA-Z\.]+$')
    if re_email.match(addr):
        return True
    else:
        return False

assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')


# 版本二：提取出Email中的名字
def name_of_email(addr):
    re_email = re.compile(r'^\<*([a-zA-Z\s]*)\>*([a-zA-Z\s]*)\@[a-zA-Z\.]+$')
    m = re_email.match(addr)
    return m.group(1)
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')