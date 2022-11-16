'''
python 全局解释器锁(Global Interpreter Lock, GIL)是一个互斥锁，它只允许一个线程来控制python解释器
python是引用计数变量进行内存管理，当某对象计数为0时则释放该对象的空间。但若多个线程同时改变引用值，就可能导致
内存泄漏，甚至在变量仍被引用的情况下其内存就释放了。
如果为每个变量添加锁，则可能导致死锁，且由于重复获取和释放锁而导致性能下降。
GIL是解释器本身的单个锁，它要求：执行任何python字节码都需要获取解释器锁。以此防止死锁，且性能开销不大。而由此
它也有效地使得任何受CPU限制的python程序都是单线程的。
GIL最大的问题是python的多线程程序并不能利用多核CPU的优势（比如一个使用了多线程的计算密集型程序仍只会在一个单
CPU上运行。
GIL只会影响到那些严重依赖CPU的程序（如计算型）。如果程序大部分只涉及I/O（如网络交互），则多线程也不会被影响。
'''

import time
import threading
from queue import Queue
import copy

def job(l, q):
    res = sum(l)
    q.put(res)

def multi_threading(l):
    threads = []
    q = Queue()
    for i in range(4):
        # 设置线程，名字为Ti
        t = threading.Thread(target=job, args=(copy.copy(l), q), name = 'T%i' % i)
        t.start()
        threads.append(t)
    # 使每个线程join到主线程上
    [t.join() for t in threads]
    res = 0
    for _ in range(4):
        res += q.get()
    print(res)

def normal(l):
    print(sum(l))

def main():
    l = list(range(1000000))
    s_t = time.time()
    normal(l * 4)
    print('normal: ', time.time() - s_t)
    m_t = time.time()
    multi_threading(l)
    print('multi_threading: ', time.time() - m_t)

if __name__ == '__main__':
    main()