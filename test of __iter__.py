class Fib():
    def __init__(self):
        self.__a = 0
        self.__b = 1
    
    def __iter__(self):  # 让类变成可迭代的，因为实例本身就是一个可迭代对象，故返回该实例本身
        return self
    
    def __next__(self):
        self.__a, self.__b = self.__b, self.__a + self.__b
        if self.__a > 100000:
            raise StopIteration
        return self.__a
f = Fib()
print(next(f))
for n in Fib():
    print(n)

