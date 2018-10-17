# encoding:utf8

from selenium.common.exceptions import TimeoutException
import time


def verify_msg_time(self, method, sleep_frequency, timeout , message=''):
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
                raise TimeoutException(msg)
        else:
            print(self.send_msg_button().is_enabled())
            break
