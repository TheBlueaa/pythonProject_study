# # 不使用tommorrow实现听歌、吃饭、聊天案例的场景
#
# import threading
#
# def task(task_name):
#     print(threading.current_thread().name + " 执行的任务为：", task_name)
#
# if __name__ == '__main__':
#     # 定义任务列表
#     task_list = ["听歌", "吃饭", "聊天"]
#     # 启动多线程完成任务列表
#     thread_list = []
#     for i in range(3):
#         thread_list.append(threading.Thread(target=task, args=(task_list[i], ), name="%s 号线程" % i))
#
#     for i in range(3):
#         thread_list[i].start()
#
#     for i in range(3):
#         thread_list[i].join()

# 使用tomorrow模块来实现听歌、吃饭和聊天
import threading
from tomorrow import threads

# 定义要执行的任务
@threads(10)
# 代表最多启动10个线程运行
def task(task_name):
    print(threading.current_thread().name + " 执行的任务为：", task_name)
if __name__ == '__main__':
    # 定义任务列表
    task_list = ["听歌", "吃饭", "聊天"]
    for i in range(3):
        task(task_list[i])