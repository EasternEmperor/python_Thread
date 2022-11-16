'''
由job3的线程可以看出，没有获取锁的线程可以正常获得cpu执行，而获取锁的则需等待锁
'''


import threading
import time

def job1():
    # global关键词用来获取外部的全局变量
    global A, lock
    lock.acquire()
    for i in range(10):
        A += 1
        print('job1: ', A)
        # time.sleep(0.1)
    lock.release()

def job2():
    global A, lock
    lock.acquire()
    for i in range(10):
        A += 10
        print('job2: ', A)
    lock.release()

def job3():
    global A
    for i in range(10):
        A += 20
        print('job3: ', A)
        # time.sleep(0.1)

def main():
    t1 = threading.Thread(target=job1)
    t2 = threading.Thread(target=job2)
    t3 = threading.Thread(target=job3)
    t3.start()
    t1.start()
    t2.start()
    t3.join()
    t1.join()
    t2.join()

if __name__ == '__main__':
    A = 0
    lock = threading.Lock()
    main()