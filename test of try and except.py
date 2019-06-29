number1 = int(input('Please input an integer:'))
number2 = int(input('Please input another integer:'))

try:
    print('try...')
    r = number1 / number2
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')

print('END')


# 用多个except语句来捕获不同类型的错误，并执行不同的动作
try:
    print('try...')
    r = number1 / int('22')
    print('result', r)
except ValueError  as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error')
finally:
    print('finally...')

print('END')


# try except跨多层调用
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally...')

main()