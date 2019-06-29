def _odd_iter():  # 创建一个奇数生成器
    n = 1
    while True:
        n = n + 2
        yield n
    return 0

def _not_divisable(n):  # 创建一个筛选函数
    return lambda x: x % n > 0

def primes(limit):
    n = 2
    it = _odd_iter()
    while n <= limit:
        yield n
        n = next(it)
        it = filter(_not_divisable(n), it)
    return 0

p = primes(100)
# i = 0
# while i < 5:
#     print(next(p))
#     i += 1
print(list(p))
