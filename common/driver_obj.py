# encoding:utf8

from selenium import webdriver
import sys

if len(sys.argv) == 1:
    URL = 'https://www.tapd.cn'
    BROWSER_NAME = 'Chrome'
elif len(sys.argv) == 2 and 'http' in sys.argv[-1]:
    URL = sys.argv[-1]
elif len(sys.argv) == 3 and 'http' in sys.argv[-1]:
    BROWSER_NAME, URL = sys.argv[-2], sys.argv[-1]
    print('driver_obj:', BROWSER_NAME)
else:
    print('退出')
    exit()


class Driver():

    def driver(self, browser_name=BROWSER_NAME):
        if browser_name == 'Chrome':
            dr = webdriver.Chrome()
        elif browser_name == 'Firefox':
            dr = webdriver.Firefox()
        elif browser_name == 'Ie':
            dr = webdriver.Ie()
        elif browser_name == 'Edge':
            dr = webdriver.Edge()
        elif browser_name == 'Safari':
            dr = webdriver.Safari()
        else:
            raise NameError(
                "Not found %s browser,You can enter 'Chrome', 'Firefox', 'Ie', 'Edge', 'Safari' ." % browser_name)
        return dr
