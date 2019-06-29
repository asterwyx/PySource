# - * - coding=utf-8 - * -
from multiprocessing import Process
import os
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))
if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',)) # 用Process类创建一个子进程
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')
    p2 = Process(target=run_proc, args=('test',))
    p2.start()
    p2.join()

# 使用进程池的方法启动大量的子进程
from multiprocessing import Pool
import time, random
def long_time_task(name): #创建一个目标函数，添加一些提示信息
    print('Run task %s (%s)' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))
if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool()
    for i in range(10):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')


import subprocess
print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)

print('divider...')

# 实现进程间通信
from multiprocessing import Queue
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()