# 导入threading模块
import threading
# 创建继承threading.Thread类的类
class MyThread(threading.Thread):
    def __init__(self, func, args, name=None):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name

    # 重写run方法
    def run(self):
        return self.func(*self.args)




# 定义要执行的任务方法
def add(x, y):
    result = x + y
    print(threading.current_thread().name +" " + str(result))
# 在main方法中启动多个线程执行任务
def main():
    # 定义两个线程
    t1 = MyThread(add, (1,2), name="t1")
    t2 = MyThread(add, (11,22), name="t2")
    # 启动线程
    t1.start()
    t2.start()

# 启动main方法
if __name__ == '__main__':
    main()