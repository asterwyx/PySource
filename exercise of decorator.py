import functools, time
def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        t1 = time.time()
        r = fn(*args, **kw)
        print('%s executed in %s ms' % (fn.__name__, 1000*(time.time() - t1 )))
        return r
    return wrapper

@metric
def fast():
    time.sleep(0.0012)

@metric
def slow(x, y, z):
    # time.sleep(0.1234)
    return x * y * z

print(fast())
print(slow(11, 22, 33))