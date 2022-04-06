import threading
import time


def action(max):
    for i in range(max):
        print(threading.current_thread().name + "%s次循环" % i)
    time.sleep(1)


def main():
    # 启动后台线程
    t1 = threading.Thread(target=action, args=(10000,), name="后台线程")

    # 在start之前，需要设置守护线程的开关
    t1.daemon = True
    # 启动后台线程
    t1.start()

    # 让主线程继续运行一会儿，打印循环输出的次数
    for i in range(10):
        print(threading.current_thread().name + "主线程循环了%s次" % i)

    print("主线程运行结束了")

if __name__ == '__main__':
    main()