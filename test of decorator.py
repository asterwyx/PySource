import functools
def log(text): # 增强now()函数的功能，在运行之前打印日志
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' %(text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2019-5-18') 
f = now
f()  
print(now.__name__)  # 拿到定义时候的名字
print(f.__name__)





