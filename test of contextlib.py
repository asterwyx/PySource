# -*- coding:utf-8 -*-
# 这是用来测试Python的上下文管理库contextlib的代码
# 首先尝试不使用contextlib提供的上下文管理器实现上下文管理
# 所谓上下文管理就是在执行一段代码之前先进行一些预处理，然后在执行这段代码之后再做一些善后工作，比如数据库操作要在之前连接数据库，文件IO也需要打开关闭文件
# 在Python的上下文管理协议中，使用__enter__作为入口，使用__exit__作为出口，即在__enter__函数中放入预处理，在__exit__函数中放入善后工作
# 一个类如果对这两个函数进行了定义，那么这个类返回的对象就是一个上下文管理器(context manager)
class Query(object):

    def __init__(self, name):
        self.name = name

    
    def __enter__(self):
        print("Begin")
        return self

    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print("Error")
        else:
            print("End")  


    def query(self):
        print("Query info about %s..." % self.name) # Python使用和C一样的占位符

# 现在我们已经编写了一个具有__enter__和__exit__函数的类模板，用它创造的对象就是上下文管理器，这里需要使用with语句来获取这个上下文管理器
with Query('Nick') as q:
    q.query()
# 执行with xxxx时会获取一个上下文管理器，并且执行__enter__函数的内容而后面的as xxx相当于把这个管理器存为一个普通变量，如果不再调用这个管理器中的函数这个地方可以省略
# 这里是使用Python提供的上下文管理协议自定义了一个上下文管理器，还是有一些麻烦，下面使用Python的上下文管理器
print("divider......")
from contextlib import contextmanager
class Student(object):
    
    def __init__(self, name):
        self.name = name
    

    def print_info(self):
        print("This is %s" % self.name)


@contextmanager
def Student_manager(name):
    print("Begin")
    yield Student(name)
    print("END")

# @contextmanager这个decorator接受一个generator，用yield语句将with ... as var需要的变量输出出去，这样with语句就可以正常工作了
with Student_manager("Nick") as s:
    s.print_info()

# 实现在执行一段代码之前先进行预处理
@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)

with tag('p'):
    print("Hello")
    print("World")
# 这里实际上是模仿了一个html标签的创建，运用这样的上下文管理就不用管html格式了，with后面的代码只需要print NavigableString即可
# 如果一个对象没有定义__enter__和__exit__函数，就需要运用closing()函数将变成一个上下文管理器
from contextlib import closing
from urllib.request import urlopen
with closing(urlopen("https://www.python.org")) as page:
    for line in page:
        print(line)
# 实际上closing也是一个经过@contextmanager修饰的decorator，写起来其实很简单
# @contextmanager
# def closing(thing):
#   try:
#       yield thing
#   finally:
#       thing.close()