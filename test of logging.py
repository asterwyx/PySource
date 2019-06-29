import logging
# def foo(s):
#     return 10 / int(s)

# def bar(s):
#     return foo(s) * 2

def foo(s):
    return 10 / int(s)

def bar(s):
    try:
        foo(s)
    except ZeroDivisionError:
        raise ValueError("s can't be 0")


def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)
    

main() # 执行该语句时出错，但logging会将错误记录下来
print('END') # 因为logging将错误记录下来了，程序会继续执行，所以该语句仍然能够执行
# 从执行窗户可以看到返回值是0，所以这个程序是正常退出的



# class FooError(ValueError):
#     pass

# def foo(s):
#     n = int(s)
#     if n==0:
#         raise FooError('invalid value: %s' % s)
#     else:
#         return 10 / n

# foo('0')

# 通过上抛错误来处理该错误