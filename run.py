#coding=utf-8

import unittest
import HTMLTestRunner
import time
import os
from loguru import logger
from config import globalparam
from public.common import sendmail
from testcase import test_1_login, test_2_workbench
from public.common.mongo_utils import MongoModel
# from BeautifulReport import BeautifulReport
from HTMLTestRunner_cn import HTMLTestRunner_cn
# from tomorrow import threads
import HTMLTestRunner_gu


path = os.path.join(os.path.abspath('.'),'report', 'logs','test_{}.log'.format(time.strftime('%Y-%m-%d')))
logger.add(path)  # 日志初始化

def run(method, test=None):
    if method == 'all':
        test_dir = './testcase'
        suite = unittest.defaultTestLoader.discover(start_dir=test_dir, pattern='test_*.py')

        now = time.strftime('%Y-%m-%d_%H_%M_%S')
        reportname = os.path.join(globalparam.report_path, 'TestResult' + now + '.html')
        with open(reportname, 'wb') as f:
            runner = HTMLTestRunner_gu.HTMLTestRunner(
                stream=f,
                title='测试报告',
                description=''
            )
            runner.run(suite)
        time.sleep(3)
        # 发送邮件
        # MongoModel().delete_customer('13800138011')
        mail = sendmail.SendMail()
        mail.send()
    if method == 'one':
        suit = unittest.TestSuite()
        suit.addTest(test)  # 把这个类中需要执行的测试用例加进去，有多条再加即可
        runner = unittest.TextTestRunner()
        runner.run(suit)

if __name__ == '__main__':
    # run('one', test_workbench.TestWorkbench("test_luandian"))
    run('all')

# def add_cases():
#     '''加载所有的测试用例'''
#     test_dir = './testcase'
#     discover = unittest.defaultTestLoader.discover(start_dir=test_dir,pattern='test*.py')
#     return discover


# @threads(3)
# def run(test_suit):
#     result = BeautifulReport(test_suit)
#     now = time.strftime('%Y-%m-%d_%H_%M_%S')
#     reportname = 'TestResult' + now + '.html'
#     result.report(filename=reportname, description='测试报告',
#                   log_path='./report/html_report')
#
#
#
# if __name__ == '__main__':
#     cases = add_cases()
#     for case in cases:
#         run(case)
