from functools import reduce
def is_palindrome(n):
    previous = n
    L = []
    while n > 0:
        L.append(n % 10)
        n = n // 10
    def add(x, y):
        return 10 * x + y
    sum = reduce(add,L)
    return sum == previous

output = list(filter(is_palindrome,range(1,1000)))
print(output)
