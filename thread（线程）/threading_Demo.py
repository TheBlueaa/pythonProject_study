import _thread
import threading
import time

global brick_list
brick_list = ["砖头1", "砖头2", "砖头3", "砖头4", "砖头5", "砖头6", "砖头7", "砖头8", "砖头9", "砖头10",
                  "砖头11", "砖头12", "砖头13", "砖头14", "砖头15", "砖头16", "砖头17", "砖头18", "砖头19", "砖头20",
                  "砖头21", "砖头22", "砖头23", "砖头24", "砖头25", "砖头26", "砖头27", "砖头28", "砖头29", "砖头30",
                  "砖头31", "砖头32", "砖头33", "砖头34", "砖头35", "砖头36", "砖头37", "砖头38", "砖头39", "砖头40",
                  "砖头41", "砖头42", "砖头43", "砖头44", "砖头45", "砖头46", "砖头47", "砖头48", "砖头49", "砖头50",
                  "砖头51", "砖头52", "砖头53", "砖头54", "砖头55", "砖头56", "砖头57", "砖头58", "砖头59", "砖头60",
                  "砖头61", "砖头62", "砖头63", "砖头64", "砖头65", "砖头66", "砖头67", "砖头68", "砖头69", "砖头70",
                  "砖头71", "砖头72", "砖头73", "砖头74", "砖头75", "砖头76", "砖头77", "砖头78", "砖头79", "砖头80",
                  "砖头81", "砖头82", "砖头83", "砖头84", "砖头85", "砖头86", "砖头87", "砖头88", "砖头89", "砖头90",
                  "砖头91", "砖头92", "砖头93", "砖头94", "砖头95", "砖头96", "砖头97", "砖头98", "砖头99", "砖头100"]

def action():
    while True:
        if len(brick_list) == 0 :
            break
        brick_list.pop() # 搬砖
        print(threading.current_thread().name + "剩余的砖：", brick_list)
        time.sleep(0.2)

def main():
    # # 启动1个线程
    # t1 = threading.Thread(target=action, args=(), name="1号码农", daemon=False) # daemon=True是守护线程，主线程运行完毕，守护线程也会自动退出
    # t1.start()
    #
    # # 启动2个线程
    # t2 = threading.Thread(target=action, args=(), name="2号码农", daemon=False)
    # t2.start()

    # 启动100个线程
    for i in range(100):
        temp = threading.Thread(target=action, args=(), name="%s号码农" % i)
        temp.start()



if __name__ == '__main__':
    main()