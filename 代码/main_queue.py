# # 入门案例
# from queue import Queue
#
# # 创建队列
# q = Queue(maxsize=10) # maxsize=10是队列的大小为10
#
# # 插入数据
# q.put(1)
# # 再次插入
# q.put("a")
#
# # 提取数据并打印
# print(q.get())
# # 再次提取
# print(q.get())

# 需求：实现厨师做10个菜，做好之后，食客开始吃菜，吃完之后，又通知厨师继续做菜，如此往复
from queue import Queue
import threading
import time
import random
#
# # 创建队列
# q = Queue(10)
# # 创建菜单
# food_menu = ["佛跳墙", "红烧狮子头", "东坡肉", "蚂蚁上树", "鱼香肉丝", "麻婆豆腐", "鱼子酱", "意大利面", "土豆丝炒肉", "银耳羹", "窝窝头", "糖醋排骨"]
#
# # 生产者厨师
# def make_lunch():
#     print("已经开始做菜了")
#     while True:
#         if q.full():
#             print("菜已经做好了！！！")
#             q.join() # 停止做菜
#
#         food_number = random.randint(0, len(food_menu) -1 )
#         q.put(food_menu[food_number])
#         print("做好了%s 菜" % food_menu[food_number])
#         time.sleep(0.1) # 控制做菜的频率
#
# # 消费者
# def eat_lunch():
#     time.sleep(10) # 等待厨师把菜做好
#     while True:
#         if q.empty():
#             print("厨师快点做点，我们饿了！")
#             time.sleep(10)
#
#         else:
#             food = q.get()
#             print("吃了%s" % food)
#             time.sleep(0.5) # 每吃一个菜都需要休息
#             q.task_done() # 通知服务员这个菜吃完了
#
# if __name__ == '__main__':
#     # 启动两个线程分别担当厨师和食客
#     cooker = threading.Thread(target=make_lunch, args=(), name="cooker")
#     eater = threading.Thread(target=eat_lunch, args=(), name="eater")
#
#     cooker.start()
#     eater.start()
from queue import Queue
import threading
import random
q = Queue(10)
food_menu = ["佛跳墙", "红烧狮子头", "东坡肉", "蚂蚁上树", "鱼香肉丝", "麻婆豆腐", "鱼子酱", "意大利面", "土豆丝炒肉", "银耳羹", "窝窝头", "糖醋排骨"]
def make_lunch():
    print("开始做饭")
    while True:
        if q.full():
            print("菜已经做好了！")
            q.join() #停止做菜
        # food_number = random.randint(0,len(food_menu) -1)
        food_number = random.randint(0, len(food_menu) - 1)
        print(food_number)
        q.put(food_menu[food_number])
        print("做好了%s菜"%food_menu[food_number])
        time.sleep(0.1)
# def eat_lunch():
#     time.sleep(1)
#     while True:
#         if q.empty():
#             print("厨师什么还不做饭？")
#         else:
#             food = q.get()
#             print("吃了%s菜"%food)
#             time.sleep(0.5)
#             q.task_done()
if __name__ == "__main__":
    cooker = threading.Thread(target=make_lunch,args=(),name="coker")
    # eater = threading.Thread(target=eat_lunch,args=(),name="eater")
    cooker.start()
    # eater.start()
