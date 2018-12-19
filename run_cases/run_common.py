# encoding:utf8

import os
import sys
import unittest
import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
TEST_CASE_DIR = BASE_DIR + '/test_case'
TEST_REPORT_DIR = BASE_DIR + '/report'
SCREENSHOT_PNG_DIR = BASE_DIR + '/screenshot_png'
PAGES_DIR = BASE_DIR + '/pages'
ALL_DIR = [BASE_DIR, \
           TEST_CASE_DIR, \
           SCREENSHOT_PNG_DIR, \
           PAGES_DIR]
sys.path.extend(ALL_DIR)


class CasesRunner():
    '''
    这个类是用于加载运行指定的测试用例，或者返回指定用例的测试套件
    '''

    def run_dir(start_dir, pattern='test*.py', top_level_dir=None, report=0):
        '''
        查找并返回指定的起始目录中的所有测试模块，递归到子目录中以查找它们并返回在其
        中找到的所有测试。仅加载与模式匹配的测试文件。
        必须可以从项目的顶层导入测试模块。如果起始目录不是顶级目录，则必须单独指定顶级目录
        :param pattern: 匹配需要测试得模块规则，test*.py 表示
        :param top_level_dir: 起始目录绝对路径
        :param report: 默认为0 ， 0 表示选择运行用例 ， 1 表示选择返回测试套件
        :return: 运行结果 或 测试套件
        '''
        cases = unittest.defaultTestLoader.discover(start_dir, pattern, top_level_dir)
        if report == 0:
            runner = unittest.TextTestRunner(verbosity=2)
            return runner.run(cases)
        elif report == 1:
            return cases
        else:
            raise ValueError('report must be 0 or 1')

    def run_cases(self, names, report=0):
        '''
        用于执行指定的用例 或 用于返回指定得测试套件
        :param names: 必须传入数组或者元组，元素可以是模块、类、方法 ,
                        传入格式1：moudleName
                        传入格式2：moudleName.testCaseClassName
                        传入格式3：moudleName.testCaseClassName.testCaseName
        :param report: 默认为0 ， 0 表示选择运行用例 ， 1 表示选择返回测试套件
        :return:  运行结果 或 测试套件
        '''
        if isinstance(names, tuple) or isinstance(names, list):
            cases = unittest.defaultTestLoader.loadTestsFromNames(names)
            if report == 0:
                runner = unittest.TextTestRunner(verbosity=2)
                return runner.run(cases)
            elif report == 1:
                return cases
            else:
                raise ValueError('report must be 0 or 1')
        else:
            raise TypeError('names must be list or tuple')


class SendEmail():
    '''
    这个类用于发送邮件，只配置了腾讯的企业邮箱，没有配置多个邮箱服务，如项目需要再进行配置。
    '''

    def __init__(self):
        '''
        配置发送邮箱服务器，发送邮箱用户名和密码，接受邮箱，主题，正文
        '''
        self.smtpserver = ''
        # 发送邮箱用户/密码
        self.user = ''
        self.password = ''
        # 发送邮箱
        self.sender = ''
        # 接收邮箱
        self.receiver = ''
        # 主题
        self.subject = ''
        # body
        self.body = ''
        self.msg = MIMEMultipart()
        self.msg['Subject'] = Header(self.subject, 'utf-8')
        self.msg['From'] = self.sender
        self.msg['To'] = self.receiver

    def file_of_email_msg(self, file_abs_path):
        '''
        添加附件
        :param file_abs_path: 添加附件的绝对路径
        '''
        with open(file_abs_path, 'rb')as send_file:
            send_file = send_file.read()
        att = MIMEText(send_file, 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        filename = os.path.basename(file_abs_path)
        att["Content-Disposition"] = 'attachment; filename=%s' % (filename)
        self.msg.attach(att)

    def body_of_email_msg(self, body='接口测试报告'):
        '''
        添加邮件正文内容
        :param body: 邮件正文内容
        '''
        body_msg = MIMEText(body, 'html', 'utf-8')
        self.msg.attach(body_msg)

    def send_email(self, smtp_type):
        '''
        发送邮件
        :param smtp_type: 选择smtp发送协议
        '''
        # smtp = SMTP()
        if smtp_type == 'ssl':
            smtp = smtplib.SMTP_SSL(self.smtpserver, port=465)
        else:
            raise ValueError(smtp_type, '请自行配置你需要的邮件服务器')
        # smtp.connect(self.smtpserver)
        try:
            smtp.login(self.user, self.password)
            smtp.sendmail(self.msg['from'], self.msg['to'], self.msg.as_string())
            smtp.quit()
        except Exception as msg:
            print(msg, '发送邮件失败')


if __name__ == "__main__":
    send = SendEmail()
    send.body = '没有正文'
    send.body_of_email_msg(send.body)
    send.file_of_email_msg(r'E:\my_github\how_to_run\how_to_run_test_case\run_suit.py')
    send.send_email('ssl')
