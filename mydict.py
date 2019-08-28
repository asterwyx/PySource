class Mydict(dict):
    """
    Simple dict but also support access as x.y style.

    >>> d1 = Mydict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Mydict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
    ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
    ...
    AttributeError: 'Mydict' object has no attribute 'empty'
    """
    def __init__(self, **kw):
        super(Mydict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Mydict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


if __name__ == '__main__':  # 此句保证文档测试只在调试时进行，若该模块是正常导入的，文档测试不会进行
    import doctest
    doctest.testmod()