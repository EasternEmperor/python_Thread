import threading
import time

# thread.join()可以让主线程在该线程thread执行结束后才往后执行
# 即join之后，主线程暂停，thread继续执行。thread结束后，主线程才继续执行

def thread_1():
    print('thread_1 starts.')
    for i in range(10):
        time.sleep(0.1)     # 睡眠0.1s
    print('thread_1 ends.')

def thread_2():
    print('thread_2 starts.')
    print('thread_2 ends.')

def main():

    # 不使用join，t1、t2和主线程输出无序
    t1 = threading.Thread(target=thread_1)
    t2 = threading.Thread(target=thread_2)
    t1.start()
    t2.start()
    print('All done.\n')

    # 在t1.start()后执行t1.join()
    # 则t1结束后，主线程才会继续执行
    t1 = threading.Thread(target=thread_1)
    t2 = threading.Thread(target=thread_2)
    t1.start()
    t1.join()
    t2.start()
    print('All done.\n')

    # 在t2.start()后执行t2.join()
    # 则t2结束后，主线程才会继续执行
    t1 = threading.Thread(target=thread_1)
    t2 = threading.Thread(target=thread_2)
    t1.start()
    t2.start()
    t2.join()
    print("All done.\n")

if __name__ == '__main__':
    main()