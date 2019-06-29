# 第一种方法，将列表生成式的[]改成()就变成了一个generator
list1 = [1,5,8,65,2,4,8,7,8,45,54,5]
generator = (x for x in list1)
x = next(generator)
y = next(generator)
print(x,y)
z = next(generator)
print(z)

# 第二种方法，对函数进行特殊修改
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b  #与函数相比，主要是修改了这儿，就变成了一个generator
        a, b = b, a+b #注意这儿的赋值写法，和C的很不一样
        n = n + 1
    return 'done'
f = fib(6)
print(next(f))
print(next(f))
print(next(f))
print(next(f))
for x in f:
    print(x)

# 利用错误捕获机制获取返回值
g = fib(7)
while True:
    try:
        x = next(g)
        print('g:',x)
    except StopIteration as e:
        print('Generator return value:',e.value)
        break