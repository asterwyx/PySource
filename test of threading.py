import time, threading

# 新线程执行的代码
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)

# 创建一个Thread实例
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name) # 打印主线程的信息

print('\ndivider...\n')

# 假定这是银行存款
balance = 0
lock = threading.Lock()

def change_it(n):
    # 先存后取，结果应该为零
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(10000):
        # 先获取锁
        lock.acquire()
        try:
            change_it(n)
        finally:
            # 修改完一定要释放锁，不然就可能会让其他的线程一直等待
            lock.release()

t1 = threading.Thread(target=change_it, args=(5,))
t2 = threading.Thread(target=change_it, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)