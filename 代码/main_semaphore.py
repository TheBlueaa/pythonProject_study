import threading


# 获取信号量对象
import time

semapfore = threading.Semaphore(500)

def action(counts):

    print("进入地铁的人数为：%s" % counts)
    # 获取信号量
    semapfore.acquire()
    # 打印入站的乘客信息
    print("%s号乘客进入地铁站台" % counts)
    time.sleep(10)
    # 释放信号量
    semapfore.release()
    # 打印出战的乘客信息
    print("%s号乘客离开地铁站台" % counts)

def main():
    # 启动1W个线程，来进入地铁
    for i in range(10000):
        threading.Thread(target=action, args=(i,)).start()

if __name__ == '__main__':
    main()