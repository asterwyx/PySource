class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a

f = Fib()

print(f[0])
print(f[1])
print(f[2])
print(f[3])