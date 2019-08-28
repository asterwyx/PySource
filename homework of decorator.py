import functools


def print_begincall(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('begin call...')
        return func(*args, **kw)

    return wrapper


def print_endcall(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('endcall!')

    return wrapper


@print_begincall
def add(x, y):
    return x + y


print(add(1, 7))
