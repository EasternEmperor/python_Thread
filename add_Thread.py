import threading

def thread_job():
    print('This is a thread of %s' % threading.current_thread(), end = '\n')

def main():
    # target为该线程要完成的工作
    thread = threading.Thread(target=thread_job, )  # 定义线程
    thread.start()  # 启动线程

    # 获取已激活的线程数: threading.active_count()
    print(threading.active_count())

    # 查看所有线程信息: threading.enumerate()
    print(threading.enumerate())

    # 查看现在正在运行的线程：threading.current_thread()
    print(threading.current_thread())

if __name__ == '__main__':
    main()