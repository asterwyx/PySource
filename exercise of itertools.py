# -*- coding:utf-8 -*-
import itertools


def pi(N):
    PI = 0
    iteral = itertools.count(start=1, step=2)  # 因为是自动变量，退出函数就会销毁，所以每次调用函数都会从1开始，保证了正确性
    for i in range(N):
        if i % 2 == 0:
            PI = PI + 4/next(iteral)
        else:
            PI = PI - 4/next(iteral)
    return PI


if __name__ == "__main__":
    print(pi(10))
    print(pi(100))
    print(pi(1000))
    print(pi(10000))
    assert 3.04 < pi(10) < 3.05
    assert 3.13 < pi(100) < 3.14
    assert 3.140 < pi(1000) < 3.141
    assert 3.1414 < pi(10000) < 3.1415
    print('ok')
