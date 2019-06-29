# type()函数
def fn(self, name='world'):
    print('Hello, %s.' % name)

Hello = type('Hello', (object,), dict(hello=fn))  # type函数用来定义一个类
h = Hello()
h.hello()
print(type(Hello))
print(type(h))


# 使用metaclass
class MylistMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

class Mylist(list, metaclass=MylistMetaclass):
    pass


test =  Mylist()
test.add(5)
test.add(1)
print(test)