# -*- coding: utf-8 -*-
def CreateCounter():
    L = [0]      
    def Counter():
        L[0] = L[0] + 1
        return L[0]
    return Counter
CounterA = CreateCounter()
print(CounterA(), CounterA(), CounterA(), CounterA(), CounterA())
CounterB = CreateCounter
if [CounterB(), CounterB(), CounterB(), CounterB()] == [1, 2, 3, 4]:
    print('测试通过！')
else:
    print('测试失败！')