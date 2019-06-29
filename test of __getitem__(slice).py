class Fib(object):
    def __getitem__(self, item):
        a, b = 1, 1
        if isinstance(item, slice):
            start = item.start
            stop = item.stop
            if start is None:
                start = 0
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
        elif isinstance(item, int):
            for x in range(item):
                a, b = b, a + b
            return a
        else:
            raise ValueError('The argument must be a slice or an integer！')


f = Fib()
print(f[0])
print(f[0:3])