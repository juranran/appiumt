import os
import unittest
import HTMLTestRunner
import time

def allCases():
    # 获取到所有的测试模块
    suite = unittest.TestLoader().discover(
        start_dir=os.path.join(os.path.dirname(__file__)),
        pattern='test_*.py',
        top_level_dir=None
    )
    return suite

def getnowtime():
    return time.strftime('%Y-%m-%d %H-%M-%S',time.localtime())

def run():
    filename = os.path.join(os.path.dirname(__file__), 'repost', getnowtime()+'repost.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='UI自动化测试',
        description='UI自动化测试报告详细信息'
    )
    runner.run(allCases())


if __name__ == '__main__':
    run()
