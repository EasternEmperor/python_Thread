import multiprocessing as mp
import threading

def job(a, b):
    print("aaaaa")

# 创建进程
def main():
    t = threading.Thread(target = job, args=(1, 2))
    p = mp.Process(target=job, args = (1, 2))
    t.start()
    p.start()
    t.join()
    p.join()

if __name__ == '__main__':
    main()