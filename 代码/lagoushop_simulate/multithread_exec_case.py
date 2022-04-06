# 导包
import unittest

import threadpool
from threadpool import ThreadPool

def discover_case():
    # 使用TestLoader加载测试用例
    tl = unittest.TestLoader()

    suite = tl.discover("./", "test*.py")
    return suite

def run_testsuite(suite):
    # 实例化TextTestRunner
    runner = unittest.TextTestRunner()

    # 使用runner运行测试套件
    result = runner.run(suite)
    return result

if __name__ == '__main__':
    # 设置线程池
    pool = ThreadPool(10)
    # 寻找测试套件
    suite = discover_case()
    # 设置任务请求（执行测试用例run_testsuite)
    requests = threadpool.makeRequests(run_testsuite, suite)
    # 把请求放入线程池中，运行起来
    for req in requests:
        print("每个线程运行的任务是什么：", req)
        pool.putRequest(req)

    pool.wait()