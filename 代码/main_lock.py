import threading
import time

result=0
lock = threading.Lock() # 获取Lock对象
def add(max):
    global result
    lock.acquire() # 加锁
    for i in range(max):
        result += result
    lock.release() # 解锁
    print(threading.current_thread().name,  result)
def main():
    t1_list = []
    for i in range(3):
        t1_list.append(threading.Thread(target=add, args=(1000000,)))
    # 启动线程
    for i in range(3):
        t1_list[i].start()


if __name__ == '__main__':
    main()