# 尝试用多线程占满CPU
import threading, multiprocessing

def loop():
    x = 0
    while True:
        x = x + 1

for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    t.start()

# 结果是多线程并不能占满CPU，因为有GIL锁的机制，所以Python实际上不能用多线程完美利用多核CPU
