# encoding:utf8

from selenium.common.exceptions import TimeoutException
import time


def verify_msg_time(method, sleep_frequency, timeout, message=''):
    '''用来判断验证码间隔时间'''
    # count_time = 0
    now_time = time.time()
    end_time = time.time() + timeout
    while True:
        if method == False:
            # count_time = count_time + 1
            # print(count_time)
            time.sleep(sleep_frequency)
            now_time = now_time + sleep_frequency
            if now_time < end_time:
                continue
            else:
                raise TimeoutException(message)
        else:
            print(method)
            break
