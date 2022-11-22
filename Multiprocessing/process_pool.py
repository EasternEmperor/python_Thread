# 进程池：mp.Pool()，将要运行的函数放入池子，Python会自动解决多进程的问题
# 且pool有返回值，而Process要自己获取

import multiprocessing as mp

def job(x):
    return x * x

def multicore():
    # mp.Pool(processes=) 定义进程池，processes为调用进程数（使用核的数量），默认为CPU的核数
    pool = mp.Pool(processes=3)

    # 用map传递任务和参数，返回一个list。
    res = pool.map(job, range(10))
    print(res)
    print(type(res))

    # 也可以用apply_async()来传递任务和参数，但是只能传递一个参数（注意,表示迭代）
    res = pool.apply_async(job, (2, ))
    print(res.get())
    # 为了传递多个参数，可以用列表来框起多个apply_async()
    res_list = [pool.apply_async(job, (i, )) for i in range(10)]
    print([res.get() for res in res_list])

if __name__ == '__main__':
    multicore()