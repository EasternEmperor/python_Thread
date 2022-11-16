import multiprocessing as mp
import threading
import time

def job(q):
    res = 0
    for i in range(10000000):
        res += i + i ** 2 + i ** 3
    q.put(res)

def multi_process():
    q = mp.Queue()
    p1 = mp.Process(target=job, args=(q, ))
    p2 = mp.Process(target=job, args=(q, ))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('multiprocessing: ', q.get() + q.get())

def multi_thread():
    # 线程之间也可以用进程的queue进行通信
    q = mp.Queue()
    t1 = threading.Thread(target=job, args=(q, ))
    t2 = threading.Thread(target=job, args=(q, ))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('multithreading: ', q.get() + q.get())

def normal():
    res = 0
    for _ in range(2):
        for i in range(10000000):
            res += i + i ** 2 + i ** 3
    print('normal: ', res)

def main():
    ns1 = time.time()
    normal()
    ns2 = time.time()
    print('normal time: ', ns2 - ns1)

    ts1 = time.time()
    multi_thread()
    ts2 = time.time()
    print('threads time: ', ts2 - ts1)

    ps1 = time.time()
    multi_process()
    ps2 = time.time()
    print('process time: ', ps2 - ps1)

if __name__ == '__main__':
    main()
