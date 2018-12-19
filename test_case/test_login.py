# encoding:utf8

import os
import sys
import unittest

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# SCREENSHOT_PNG_DIR = BASE_DIR + '/screenshot_png'
# PAGES_DIR = BASE_DIR + '/pages'
#
# ALL_DIR = [BASE_DIR, \
#            SCREENSHOT_PNG_DIR, \
#            PAGES_DIR]
# sys.path.extend(ALL_DIR)
from pages.login_page import LoginAction
from common.driver_obj import *


class LoginCase(unittest.TestCase):

    def setUp(self):
        self.dr = Driver().driver()

    def test_login_success(self):
        username = ''
        password = ''
        login_page = LoginAction(self.dr, path='/cloud_logins/login')
        home_page = login_page.login(username, password)

        # try:
        #     text = home_page.get_real_name()
        #     print(text)
        #     self.assertEqual(expected_result, text)
        # except AssertionError as msg:
        #     raise AssertionError(msg)
        # finally:
        #     home_page.login_out()

if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(LoginCase('test_login_success'))
    runner = unittest.TextTestRunner()
    runner.run(suit)