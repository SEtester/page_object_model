# encoding:utf8

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)
from run_cases.run_common import *
from run_cases.HTMLTestRunner import HTMLTestRunner

# 冒烟测试用例集
cases = ['test_login.LoginCase.test_login_success']


run = CasesRunner()
cases = run.run_cases(cases, report=1)


# 指定测试用例为当前文件夹下的 test_case 目录
now = time.strftime("%Y-%m-%d %H_%M_%S")
filename = os.path.basename(os.path.abspath(__file__)).split('.')[0]
file_abs_path = TEST_REPORT_DIR + '/' + filename + ' ' + now + 'result.html'
fp = open(file_abs_path, 'wb')

runner = HTMLTestRunner(stream=fp, title='测试报告', description='用例执行情况：')
runner.run(cases)

# send = SendEmail()
# send.body = 'BVT测试报告'
# send.body_of_email_msg(send.body)
# send.file_of_email_msg(file_abs_path)
# send.send_email('ssl')
