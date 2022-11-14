import threading
import time
from queue import Queue

# 用Queue()数据类型来保存线程中要返回的值

# 将列表每个值计算平方，存入q中
def cal(l, q):
    for i in range(len(l)):
        l[i] = l[i] * l[i]
    q.put(l)

# 创建四个线程计算
def main():
    nums = [[1, 2, 3, 4], [4, 3, 2, 1], [1, 1, 1, 1], [2, 2, 2, 2]]
    q = Queue()
    threads = []
    # 创建并启动线程
    for i in range(4):
        # target为线程要执行的任务，args为该任务（函数）需要的参数
        t = threading.Thread(target=cal, args=(nums[i], q))
        t.start()
        threads.append(t)
    # 线程join到主线程
    for i in range(4):
        threads[i].join()
    # 将q中的内容保存到另一个列表中
    res = []
    for _ in range(4):
        # Queue.get()按顺序从队列中取出一个值
        res.append(q.get())
    print(res)

if __name__ == '__main__':
    main()